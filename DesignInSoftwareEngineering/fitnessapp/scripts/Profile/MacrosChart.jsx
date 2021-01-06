import React, { useState, useEffect } from 'react';

import { PieChart, Pie, Sector, Cell, Tooltip } from 'recharts';

export function MacrosChart(props) {
    const profileDetail = props.profileDetail;
    
    const data = [
                { name: "Max Protein", Macros: profileDetail.maxProt },
                { name: "Max Carb", Macros: profileDetail.maxCarb },
                { name: "Max Fat", Macros: profileDetail.maxFat },
             ];
    const COLORS = ['#0088FE', '#00C49F', '#FFBB28'];
    const RADIAN = Math.PI / 180;
    const renderCustomizedLabel = ({
        cx, cy, midAngle, innerRadius, outerRadius, percent, index,
        }) => {
        const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
        const x = cx + radius * Math.cos(-midAngle * RADIAN);
        const y = cy + radius * Math.sin(-midAngle * RADIAN);

         return (
                    <text x={x} y={y} fill="white" textAnchor={x > cx ? 'start' : 'end'} dominantBaseline="central">
                     {`${(percent * 100).toFixed(0)}%`}
                     </text>
                );
        };
    
    return (
        <div id = 'MacrosChartBox'>
            <h3>Recommended Macros<br/>Max Calories: { profileDetail.maxCal }</h3>
            <div className ="Canvasdiv"> 
                    <canvas className = "CanvasProt"/><label> : Max Protein </label> <br/>
                    <canvas className = "CanvasCarb"/><label> : Max Carb </label> <br/>
                    <canvas className = "CanvasFat"/><label> : Max Fat </label> <br/>
            </div>
            <div id = 'MacrosChart'>
                <PieChart width={500} height={500}>
                    <Pie
                        dataKey="Macros"
                        isAnimationActive={false}
                        data={data}
                        cx={200}
                        cy={200}
                        outerRadius={80}
                        fill="#002db3"
                        labelLine={false}
                        label={renderCustomizedLabel}
                    >
                    {
                        data.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)
                    }
                    </Pie>
                <Tooltip />
                </PieChart>
            </div>
        </div>
    )
}