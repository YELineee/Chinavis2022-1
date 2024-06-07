<template>
   <div style="padding: 10px">
     <div style="border: 3px solid black; border-radius: 10px;background-color: rgba(255, 255, 255, 0.9);">
       <div ref="chartContainer"></div>
       <div id="tooltip"></div>
     </div>
   </div>
 </template>
 
 <script setup>
 import * as d3 from "d3";
 import axios from "axios";
 import { ref, onMounted } from "vue";
 
 const width = window.innerWidth ;
 const height = window.innerHeight;
 const dpi = window.devicePixelRatio;
 
 let canvas = null;
 let context = null;
 let simulation = null;
 let nodes = null;
 let links = null;
 
 const chartContainer = ref(null);
 
 // console.log(nodes, links);
 
 const draw = () => {
   const nodeSize = {
     IP: 5,
     IP_CIDR: 5,
     ASN: 5,
     Cert: 5,
     Domain: 5,
     Whois_Name: 5,
     Whois_Email: 5,
     Whois_Phone: 5,
     default: 5,
   };
 
   const nodeColor = {
     IP: "#2196F3",
     IP_CIDR: "#3F51B5",
     ASN: "#673AB7",
     Cert: "#E91E63",
     Domain: "#FFC107",
     Whois_Name: "#4CAF50",
     Whois_Email: "#FF5722",
     Whois_Phone: "#9C27B0",
     default: "#ffffff",
   };
 
   const linkWidth = {
     r_cert: "0.8",
     r_subdomain: "0.8",
     r_dns_a: "0.8",
     r_request_jump: "0.8",
     r_whois_name: "0.6",
     r_whois_email: "0.6",
     r_whois_phone: "0.6",
     r_cert_chain: "0.4",
     r_dns_cname: "0.4",
     r_cidr: "0.2",
     r_asn: "0.2",
     default: "0.1",
   };
 
   const linkColor = {
     r_cert: "#999",
     r_subdomain: "#999",
     r_dns_a: "#999",
     r_request_jump: "#999",
     r_whois_name: "#3F51B5",
     r_whois_email: "#3F51B5",
     r_whois_phone: "#3F51B5",
     r_cert_chain: "#3F51B5",
     r_dns_cname: "#3F51B5",
     r_cidr: "#3F51B5",
     r_asn: "#3F51B5",
     default: "#3F51B5",
   };
 
   if (!context || !canvas) return;
   context.clearRect(0, 0, width, height);
 
   context.save();
   context.globalAlpha = 0.8;
   context.beginPath();
   links.forEach((link) => {
     drawLink(link);
     context.lineWidth = linkWidth[link.relation] || linkWidth["default"];
     context.strokeStyle = linkColor[link.relation] || linkColor["default"];
   });
   context.stroke();
   context.restore();
 
   context.save();
   context.globalAlpha = 1;
   nodes.forEach((node) => {
     context.beginPath();
     drawNode(node);
     context.fillStyle = nodeColor[node.attribute] || nodeColor["default"];
     context.arc(
       node.x,
       node.y,
       nodeSize[node.attribute] || nodeSize["default"],
       0,
       2 * Math.PI,
       false,
     );
     context.strokeStyle = "#fff";
     context.fill();
     context.stroke();
   });
   context.restore();
 };
 
 const drawLink = (d) => {
   context.moveTo(d.source.x, d.source.y);
   context.lineTo(d.target.x, d.target.y);
 };
 
 const drawNode = (d) => {
   context.moveTo(d.x + 5, d.y);
   context.arc(d.x, d.y, 5, 0, 2 * Math.PI);
 };
 
 const dragstarted = (event) => {
   if (!event.active) simulation.alphaTarget(0.3).restart();
   event.subject.fx = event.subject.x;
   event.subject.fy = event.subject.y;
 };
 
 const dragged = (event) => {
   event.subject.fx = event.x;
   event.subject.fy = event.y;
 };
 
 const dragended = (event) => {
   if (!event.active) simulation.alphaTarget(0);
   event.subject.fx = null;
   event.subject.fy = null;
 };
 
 const showTooltip = (node) => {
   const tooltip = d3.select("#tooltip");
   const transform = d3.zoomTransform(canvas); // 获取缩放变换后的坐标值
   tooltip
     .style("display", "block")
     .style("left", `${transform.applyX(node.x) + 20}px`) // 使用 applyX 方法转换 x 坐标
     .style("top", `${transform.applyY(node.y) - 40}px`) // 使用 applyY 方法转换 y 坐标
     .html(node.id);
 };
 
 const hideTooltip = () => {
   const tooltip = d3.select("#tooltip");
   tooltip.style("display", "none");
 };
 
 onMounted(async () => {
   try {
     const response = await axios.get(
       "http://127.0.0.1:8000/data/read_nodes?id=CAG2",
     );
     const fetchedData = response.data;
     nodes = fetchedData.nodes;
     links = fetchedData.links;
 
     canvas = d3
       .select(chartContainer.value)
       .append("canvas")
       .attr("width", dpi * width)
       .attr("height", dpi * height)
       .attr("style", `width: ${width}px; max-width: 100%; height: full;`)
       .node();
 
     context = canvas.getContext("2d");
     context.scale(dpi, dpi);
 
     simulation = d3
       .forceSimulation(nodes)
       .force(
         "link",
         d3
           .forceLink(links)
           .distance(50)
           .id((d) => d.id),
       )
       .force("center", d3.forceCenter(width / 2, height / 2))
       .force("collision", d3.forceCollide().radius(2)) // Prevent nodes overflow
       .force("charge", d3.forceManyBody().strength(-50))
       .on("tick", draw);
 
     // d3.select(canvas).call(
     //   d3
     //     .drag()
     //     .subject((event) => {
     //       const [px, py] = d3.pointer(event, canvas);
     //       return d3.least(nodes, ({ x, y }) => {
     //         const dist2 = (x - px) ** 2 + (y - py) ** 2;
     //         if (dist2 < 400) return dist2;
     //       });
     //     })
     //     .on("start", dragstarted)
     //     .on("drag", dragged)
     //     .on("end", dragended),
     // );
 
     d3.select(canvas).call(
       d3
         .zoom()
         .scaleExtent([0.1, 5])
         .on("zoom", (event) => {
           const { transform } = event;
           context.save();
           context.clearRect(0, 0, width, height);
           context.translate(transform.x, transform.y);
           context.scale(transform.k, transform.k);
           draw();
           context.restore();
         }),
     );
 
     d3.select(canvas).on("mousemove", (event) => {
       // 获取缩放变换后的坐标值
       const { offsetX, offsetY } = event;
       const transform = d3.zoomTransform(canvas);
       const [mx, my] = transform.invert([offsetX, offsetY]);
 
       // 计算节点与鼠标的距离
       const node = d3.least(nodes, ({ x, y }) => {
         const dist2 = (x - mx) ** 2 + (y - my) ** 2;
         if (dist2 < 400) return dist2;
       });
 
       // 显示或隐藏提示框
       if (node) {
         showTooltip(node);
       } else {
         hideTooltip();
       }
     });
   } catch (error) {
     console.error("Error fetching data:", error);
   }
 });
 </script>
 
 <style>
 #tooltip {
   position: absolute;
   display: none;
   background: #333;
   color: #fff;
   padding: 5px;
   border-radius: 5px;
   font-size: 10px;
 }
 </style>
 