#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
int calLSD(int num){
    if(num < 10){
        return num;
    }
    else if(num >= 10 && num < 100){
        return num / 10;
    }
    else if(num >= 100 && num < 1000){
        return num / 100;    
    }    
    else{
        return num / 1000;   
    }
}
int calMod(int num){
     if(num < 10){
        return num;
    }
    else if(num >= 10 && num < 100){
        return num % 10;
    }
    else if(num >= 100 && num < 1000){
        return num % 100;    
    }    
    else{
        return num % 1000;   
    }
}

int sort(int numbers[], size_t numbers_len){
    for(int i = 0; i < numbers_len; i++){
        for(int j = i; j < numbers_len; j++){
            // 가장 왼쪽 자리부터 비교
            if(calLSD(numbers[i]) == calLSD(numbers[j])){
                int tmp1 = numbers[i];
                int tmp2 = numbers[j];
                while(1){
                    tmp1 = calMod(tmp1);
                    tmp2 = calMod(tmp2);
                    if(calLSD(tmp1) < calLSD(tmp2)){ // 다르다면
                         int tmp = numbers[i];
                         numbers[i] = numbers[j];
                         numbers[j] = tmp;
                        break;
                    }
                    else if(calLSD(tmp1) < calLSD(tmp2)){
                        break;
                    }
                    else{ // 같다면
                        if(calLSD(tmp1) < 10 && calLSD(tmp2) < 10){
                            break;
                        }
                    }
                }
            }
            else if(calLSD(numbers[i]) < calLSD(numbers[j])){
                int tmp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = tmp;
            }
        }
    }
}
// numbers_len은 배열 numbers의 길이입니다.
char* solution(int numbers[], size_t numbers_len) {
    sort(numbers, numbers_len);
    for(int i = 0 ; i < numbers_len; i++){
        printf("%d ", numbers[i]);
    }
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char** answer = (char**)malloc(numbers_len);
    for(int i = 0; i < numbers_len; i++){
        answer[i] = (char*)malloc(4);
    }
     sprintf(answer[0], "%d", numbers[0]);
    for(int i = 1 ; i < numbers_len; i++){
        sprintf(answer[i], "%d", numbers[i]);
        strcat(answer[0], answer[i]);
    }
    
    return answer[0];
}