//
//  main.swift
//  220225_3
//
//  Created by Park Gyurim on 2022/02/25.
//

import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var answer = 1
    var numOfClothes : [String : Int] = [:]
    
    for c in clothes {
        if let _ = numOfClothes[c[1]] { numOfClothes[c[1]]! += 1 }
        else { numOfClothes[c[1]] = 1 }
    }
    
    let nums : [Int] = numOfClothes.map { key, value in return value }
    
    nums.forEach { answer *= ($0 + 1) }
    
    return answer - 1
}

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["mask", "face"]]))

// [1, 2, 1]
// (1 + 1) * (2 + 1) * (1 * 1) - 1 = 11
// 각 옷 종률 + 1 : 안입는 경우
// -1 : 아무것도 안입은 경우
