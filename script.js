var svg = d3.select("svg"),
        margin = 200,
        width = svg.attr("width") - margin,
        height = svg.attr("height") - margin

    svg.append("text")
       .attr("transform", "translate(100,0)")
       .attr("x", 50)
       .attr("y", 50)
       .attr("font-size", "30px")
       .text("Fahrgastzahlen")

    var xScale = d3.scaleBand().range([0, width]).padding(0.4),
        yScale = d3.scaleLinear().range([height, 0]);

    var g = svg.append("g")
               .attr("transform", "translate(" + 100 + "," + 100 + ")");


    d3.queue()
    .defer(d3.csv, "test-month.csv") //2020
    .defer(d3.csv, "test-month.csv") //2019
    .await(function(error, data2020, data2019) {
        if (error) throw error;

        xScale.domain(data2020.map(function(d) { return d.date; }));
        yScale.domain([0, d3.max(data2020, function(d) { return d.transported_people; })]);

        g.append("g")
         .attr("transform", "translate(0," + height + ")")
         .call(d3.axisBottom(xScale)
            .tickFormat((d) => {
                var delimiter = d.split(".");
                var d1 = new Date(Number(delimiter[2]), Number(delimiter[1]) -1, Number(delimiter[0]));
                return d3.timeFormat("%d.%m")(d1)
            }))
         .append("text")
         .attr("y", height - 250)
         .attr("x", width - 100)
         .attr("text-anchor", "end")
         .attr("stroke", "black")
         .text("Date");

        g.append("g")
         .call(d3.axisLeft(yScale).tickFormat(function(d){
             return d;
         })
         .ticks(10))
         //delete y-axis
         .call(g => g.select(".domain")
         .remove())
         //
         .append("text")
         .attr("transform", "rotate(-90)")
         .attr("y", 6)
         .attr("dy", "-5.1em")
         .attr("text-anchor", "end")
         .attr("stroke", "black")
         .text("Transported People");

        g.selectAll(".bar")
         .data(data2020)
         .enter().append("rect")
         .attr("class", "bar")
         .attr("x", function(d) { return xScale(d.date); }) //berechnet x werte
         .attr("y", function(d) { return yScale(d.transported_people); })
         .attr("width", xScale.bandwidth())
         .attr("height", function(d) { return height - yScale(d.transported_people); });

         g.selectAll(".bar2")
         .data(data2019)
         .enter().append("rect")
         .attr("class", "bar2")
         .attr("x", function(d) { return xScale(d.date) + 10; })
         .attr("y", function(d) { return yScale(d.transported_people); })
         .attr("width", xScale.bandwidth())
         .attr("height", function(d) { return height - yScale(d.transported_people); });


         //bruchi de fr kreise und info kaste
         g.selectAll(".bar2")
         .data(data2019)
         .enter().append("circle")
         .attr("class", "circle")
         .attr("x", function(d) { return xScale(d.date); }) //berechnet x werte
         .attr("y", function(d) { return yScale(d.transported_people); })
         .attr("width", xScale.bandwidth())
         .attr("height", function(d) { return height - yScale(d.transported_people); });
    
        });
