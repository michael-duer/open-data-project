const massnahmenMaerz = [
    {
    date: "14.03.2021",
    text: "Veranstaltungen verboten"
    },
    {
    date: "16.03.2021",
    text: "Lockdown"
    },
    {
    date: "24.03.2021",
    text: "Lockdown vorbei"
    }
    ];
    
    g.selectAll('circle')
    .data(massnahmenMaerz)
    .enter()
    .append('circle')
    .attr("r", 10)
    .attr('cx', function(d){ return xScale(d.date)})
    .attr('cy', function(y){ return yScale(0)})
    .append('rect udr polygon udr so')