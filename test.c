#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define HOME 0

struct City {
    struct City* next;
    char* name;
};

char * stArrCities[] = {"서울","경기","인천","강원","경북","경남","부산","전북","전남","충북","충남","제주"};

int main(){
    struct City arrCities[12];
    int arrConnected[12];

    struct City* pCurrent;

    srand(time(NULL));

    int i = 0, temp;
    for ( i=0; i<12; i++ ) {
        struct City temp;
        temp.next = NULL;
        temp.name = stArrCities[i];
        arrCities[i] = temp;
        arrConnected[i] = i;
    }

    // 섞는 중..
    for ( i=0; i<12; i++ ) {
        int iShuffleIndex = rand() % 12;
        temp = arrConnected[i];
        arrConnected[i] = arrConnected[iShuffleIndex];
        arrConnected[iShuffleIndex] = temp;
    }

    // 연결하는 중...
    for ( i=0; i<12-1; i++ ) {
        arrCities[arrConnected[i]].next = &arrCities[arrConnected[i+1]];
    }

    // 여행을 가볼까요?
    pCurrent = &arrCities[arrConnected[0]];
    printf("%s에서부터 출발!\n", pCurrent->name);

    for ( pCurrent=pCurrent->next; pCurrent->next != NULL; pCurrent=pCurrent->next ) {
        printf("%s찍고\n", pCurrent->name);
    }

    printf("여행 끝!\n");

    return HOME;
}