<template>
  <div style="padding: 10px">
    <div style="border: 3px solid black; border-radius: 10px">
      <div ref="chartContainer"></div>
    </div>
  </div>
</template>

<script>
import * as d3 from "d3";
import data from "../../backend/ipynb/sad/sad.json";

export default {
  data() {
    return {
      width: window.innerWidth - 30,
      height: window.innerHeight - 30,
      color: d3.scaleOrdinal(d3.schemeCategory10),
      dpi: window.devicePixelRatio,
      simulation: null,
      canvas: null,
      context: null,
      nodes: data.nodes,
      links: data.links,
    };
  },
  methods: {
    draw() {
      const context = this.context;
      const nodes = this.nodes;
      const links = this.links;

      context.clearRect(0, 0, this.width, this.height);

      context.save();
      context.globalAlpha = 0.6;
      context.strokeStyle = "#999";
      context.beginPath();
      links.forEach(this.drawLink);
      context.stroke();
      context.restore();

      context.save();
      context.strokeStyle = "#fff";
      context.globalAlpha = 1;
      nodes.forEach((node) => {
        context.beginPath();
        this.drawNode(node);
        context.fillStyle = this.color(node.group);
        context.strokeStyle = "#fff";
        context.fill();
        context.stroke();
      });
      context.restore();
    },
    drawLink(d) {
      this.context.moveTo(d.source.x, d.source.y);
      this.context.lineTo(d.target.x, d.target.y);
    },
    drawNode(d) {
      this.context.moveTo(d.x + 5, d.y);
      this.context.arc(d.x, d.y, 5, 0, 2 * Math.PI);
    },
    dragstarted(event) {
      if (!event.active) this.simulation.alphaTarget(0.3).restart();
      event.subject.fx = event.subject.x;
      event.subject.fy = event.subject.y;
    },
    dragged(event) {
      event.subject.fx = event.x;
      event.subject.fy = event.y;
    },
    dragended(event) {
      if (!event.active) this.simulation.alphaTarget(0);
      event.subject.fx = null;
      event.subject.fy = null;
    },
  },
  mounted() {
    const chartContainer = this.$refs.chartContainer;

    this.canvas = d3
      .select(chartContainer)
      .append("canvas")
      .attr("width", this.dpi * this.width)
      .attr("height", this.dpi * this.height)
      .attr("style", `width: ${this.width}px; max-width: 100%; height: auto;`)
      .node();

    this.context = this.canvas.getContext("2d");
    this.context.scale(this.dpi, this.dpi);

    this.simulation = d3
      .forceSimulation(this.nodes)
      .force(
        "link",
        d3.forceLink(this.links).id((d) => d.id),
      )
      .force("charge", d3.forceManyBody())
      .force("center", d3.forceCenter(this.width / 2, this.height / 2))
      .force("collision", d3.forceCollide().radius(5)) // Add collision force to prevent nodes from overflowing the screen
      .on("tick", this.draw);

    d3.select(this.canvas).call(
      d3
        .drag()
        .subject((event) => {
          const [px, py] = d3.pointer(event, this.canvas);
          return d3.least(this.nodes, ({ x, y }) => {
            const dist2 = (x - px) ** 2 + (y - py) ** 2;
            if (dist2 < 400) return dist2;
          });
        })
        .on("start", this.dragstarted)
        .on("drag", this.dragged)
        .on("end", this.dragended),
    );
  },
  beforeDestroy() {
    this.simulation.stop();
  },
};
</script>
