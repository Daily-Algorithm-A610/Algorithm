/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/172927
 * 완탐으로 풀었는데 왜 실패함?
 * 진짜 모름
 * minerals가 고작 50개 이하로 나약하길래 완탐 했습니다.
 */
function solution(picks, minerals) {
  var answer = -1;

  mine(picks, minerals, 0, 0);

  return answer;

  function mine(picks, minerals, mIndex, _count) {
    for (let pick = 0; pick < picks.length; pick++) {
      let count = _count; // 이거 그냥 count를 써버렸더니 초기화가 안되는 거였음 ㅎㅎ;
      if (picks[pick] == 0) {
        continue;
      } else {
        for (let i = mIndex; i < mIndex + 5; i++) {
          if (i < minerals.length) {
            count += getTired(pick, minerals[i]);
          }
        }
        picks[pick]--;

        if (
          mIndex + 5 < minerals.length &&
          picks[0] + picks[1] + picks[2] != 0
        ) {
          mine(picks, minerals, mIndex + 5, count);
        } else {
          if (answer == -1 || count < answer) {
            answer = count;
          }
        }
        picks[pick]++;
      }
    }
  }

  function getTired(pick, mineral) {
    switch (pick) {
      case 0:
        return 1;
      case 1:
        if (mineral == "diamond") {
          return 5;
        } else {
          return 1;
        }
      case 2:
        switch (mineral) {
          case "diamond":
            return 25;
          case "iron":
            return 5;
          case "stone":
            return 1;
        }
    }
  }
}
