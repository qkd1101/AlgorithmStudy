//
//  main.swift
//  220225_3
//
//  Created by Park Gyurim on 2022/02/25.
//

import Foundation

func Combination(_ arr: [Int], _ r: Int, _ res: inout [[Int]], _ now: [Int] = [Int]()) {
    let n = arr.count
    guard n > 0 else { return }
    
    if r == 0 { res.append(now) }
    else if n == r { res.append(now + arr) }
    else {
        Combination(Array(arr[1...]), r - 1, &res, now + [arr.first!])
        Combination(Array(arr[1...]), r, &res, now)
    }
}

func solution(_ clothes:[[String]]) -> Int {
    var answer = 0
    var numOfClothes : [String : Int] = [:]
    var combinations : [[Int]] = []
    
    for c in clothes {
        if let _ = numOfClothes[c[1]] { numOfClothes[c[1]]! += 1 }
        else { numOfClothes[c[1]] = 1 }
    }
    
    let nums : [Int] = numOfClothes.map { key, value in return value }

    for r in 1...nums.count { Combination(nums, r, &combinations) }
    var result : [Int] = []
    var temp = 0
    for n in combinations {
        temp = 1
        n.forEach { temp *= $0 }
        answer += temp
    }
   
    return answer
}
// [1], [2], [1], [1, 2], [1, 1], [2, 1], [1, 2, 1]
// 1 + 2 + 1 + 1*2 + 1*1 + 2*1 + 1*2*1 = 11
