function solution(participant, completion) {
  participant.sort();
  completion.sort();
  for (let com in completion) {
    return participant.filter((part) => part !== com);
  }
}
let part = ["leo", "kiki", "eden"];
let comp = ["eden", "kiki"];
console.log(solution(part, comp));
