const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let line_idx = 0;
const case_num = Number(input[line_idx++]);
for (let case_idx = 0; case_idx < case_num; case_idx ++) {
	const n = Number(input[line_idx++]);
	let closet = new Map();
	
	for (let i = 0; i < n; i++) {
		const [wear_name, wear_type] = input[line_idx++].split(" ");
		if (closet.has(wear_type)) {
			closet.get(wear_type).add(wear_name);
		} else {
			closet.set(wear_type, new Set([wear_name]));
		}
	}
		
	// 계산
	let total_case = 1;
	let key_size = closet.size;
	for (const set_value of closet.values()) {
		total_case *= (set_value.size + 1)
	}
	total_case -= 1
	
	// 출력
	console.log(total_case)
}
