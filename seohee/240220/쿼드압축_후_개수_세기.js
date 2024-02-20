// 프로그래머스
// 쿼드압축 후 개수 세기

// https://school.programmers.co.kr/learn/courses/30/lessons/68936?language=javascript#

function solution(arr) {
  const answer = getZeroOneCount(0, 0, arr.length, arr);
  return answer.counter;
}

function getZeroOneCount(x, y, size, arr) {
  const answer = {
    counter: [0, 0],
    isCompressable: false,
  };
  if (size == 1) {
    answer.counter[arr[x][y]]++;
    answer.isCompressable = true;
    return answer;
  }
  const part1 = getZeroOneCount(x, y, size / 2, arr);
  const part2 = getZeroOneCount(x, y + size / 2, size / 2, arr);
  const part3 = getZeroOneCount(x + size / 2, y, size / 2, arr);
  const part4 = getZeroOneCount(x + size / 2, y + size / 2, size / 2, arr);

  // 모두 압축 가능
  if (
    part1.isCompressable &&
    part2.isCompressable &&
    part3.isCompressable &&
    part4.isCompressable
  ) {
    const sumX =
      part1.counter[0] + part2.counter[0] + part3.counter[0] + part4.counter[0];
    if (sumX == 0 || sumX == 4) {
      return part1;
    }
  }
  answer.counter[0] =
    part1.counter[0] + part2.counter[0] + part3.counter[0] + part4.counter[0];
  answer.counter[1] =
    part1.counter[1] + part2.counter[1] + part3.counter[1] + part4.counter[1];
  answer.isCompressable = false;
  return answer;
}
