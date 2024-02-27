// https://school.programmers.co.kr/learn/courses/30/lessons/86971
// 어떻게 해야할지 몰라서 그냥 완탐했는데 이게 되네................................


function solution(n, wires) {
    var answer;
    const adj = [];
    
    for (let i = 0; i < n+1; i++) {
        adj[i] = [];
    }
    for (let wire of wires) { 
        adj[wire[0]].push(wire[1]);
        adj[wire[1]].push(wire[0]);
    }
    let selectedWire = [1,3];
    function bfs(a) {
        let index = 0;
        const visited = new Set();
        let queue = [a];
        
        while(index < queue.length ){
            visited.add(queue[index]);
            for(let node of adj[queue[index]]) {
                if(!visited.has(node) && !(node == selectedWire[0] && [queue[index]] == selectedWire[1]) 
                   && !(node == selectedWire[1] && [queue[index]] == selectedWire[0])){
                    visited.add(node);
                    queue.push(node);
                }
            }
            index++;
        }
        return visited.size;
    }
    
    for (let wireIndex= 0; wireIndex< n-1; wireIndex++) {
        selectedWire = wires[wireIndex];
        const a = bfs(selectedWire[0])
        const b = bfs(selectedWire[1])
        if(answer == undefined || Math.abs(a-b) < answer) {
            answer = Math.abs(a-b)
        }
    }
    
    return answer;
}