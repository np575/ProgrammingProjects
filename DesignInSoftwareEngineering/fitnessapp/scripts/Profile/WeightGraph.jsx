import React from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,} from 'recharts';
export function WeightGraph(props) {
    const userWeight = props.userWeight;
    const goal_weight=props.goal_weight;
    const date = props.date;
    const weight_data = [
        { date: date[props.date.length-7], UserWeight: userWeight[ userWeight.length - 7], GoalWeight: goal_weight },
        { date: date[props.date.length-6], UserWeight: userWeight[ userWeight.length - 6], GoalWeight: goal_weight },
        { date: date[props.date.length-5], UserWeight: userWeight[ userWeight.length - 5], GoalWeight: goal_weight },
        { date: date[props.date.length-4], UserWeight: userWeight[ userWeight.length - 4], GoalWeight: goal_weight },
        { date: date[props.date.length-3], UserWeight: userWeight[ userWeight.length - 3], GoalWeight: goal_weight },
        { date: date[props.date.length-2], USerWeight: userWeight[ userWeight.length - 2], GoalWeight: goal_weight },
        { date: date[props.date.length-1], UserWeight: userWeight[ userWeight.length - 1], GoalWeight: goal_weight },
    ];
   
     return (
        <div className = 'WeightGraph'>
            <LineChart
            width={500}
            height={300}
            data={weight_data}
            margin={{ top: 5, right: 30, left: 20, bottom: 5, }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="UserWeight" stroke="#8884d8" activeDot={{ r: 8 }} />
        <Line type="monotone" dataKey="GoalWeight" stroke="#82ca9d" />
      </LineChart>
        </div>
    );
}