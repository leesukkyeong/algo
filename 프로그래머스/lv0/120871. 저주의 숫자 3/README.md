# [level 0] 저주의 숫자 3 - 120871 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120871) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.</p>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">10진법</th>
<th style="user-select: auto;">3x 마을에서 쓰는 숫자</th>
<th style="user-select: auto;">10진법</th>
<th style="user-select: auto;">3x 마을에서 쓰는 숫자</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">1</td>
<td style="user-select: auto;">6</td>
<td style="user-select: auto;">8</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">2</td>
<td style="user-select: auto;">7</td>
<td style="user-select: auto;">10</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">3</td>
<td style="user-select: auto;">4</td>
<td style="user-select: auto;">8</td>
<td style="user-select: auto;">11</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">4</td>
<td style="user-select: auto;">5</td>
<td style="user-select: auto;">9</td>
<td style="user-select: auto;">14</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">5</td>
<td style="user-select: auto;">7</td>
<td style="user-select: auto;">10</td>
<td style="user-select: auto;">16</td>
</tr>
</tbody>
      </table>
<p style="user-select: auto;">정수 <code style="user-select: auto;">n</code>이 매개변수로 주어질 때, <code style="user-select: auto;">n</code>을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">n</code> ≤ 100</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">n</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">15</td>
<td style="user-select: auto;">25</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">40</td>
<td style="user-select: auto;">76</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">15를 3x 마을의 숫자로 변환하면 25입니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">40을 3x 마을의 숫자로 변환하면 76입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges