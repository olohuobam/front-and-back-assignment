#include <stdio.h>



/**
 * main - A program that will read an array of 200 characters and display to the screen a count of the occurrences of 
 * each of the five vowels (a, I , e ,o , u) in an array
 * @return : Return 0 on success
 */
int main(){
    char str[200];
    int a_count = 0, e_count = 0, i_count = 0, o_count = 0, u_count = 0;
    
    printf("Enter a string (max 200 characters): ");
    fgets(str, 200, stdin); 
    
    /* Loop */
    for (int j = 0; str[j] != '\0'; j++) {
        char ch = str[j];
        switch (ch) {
            case 'a':
            case 'A':
                a_count++;
                break;
            case 'e':
            case 'E':
                e_count++;
                break;
            case 'i':
            case 'I':
                i_count++;
                break;
            case 'o':
            case 'O':
                o_count++;
                break;
            case 'u':
            case 'U':
                u_count++;
                break;
            default:
                break;
        }
    }
    
    printf("\nVowel counts:\n"
    );
    printf("A/a: %d\n", a_count);
    printf("E/e: %d\n", e_count);
    printf("I/i: %d\n", i_count);
    printf("O/o: %d\n", o_count);
    printf("U/u: %d\n", u_count);

    return 0;

    /*.....END.....*/
}
