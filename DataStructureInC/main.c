#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_LENGTH 256
#define MAX_FIELDS 5 

struct clip *build_a_lst();
struct clip *append();
int find_length();
void print_lst();
void split_line();
void free_lst();

struct clip {
  int views;
  char *user;
  char *time;
  char *duration;
  char *title;
  struct clip *next;
} *head;

int main(int argc, char **argv) {
  int n;
  head = build_a_lst(*(argv+1));
  n = find_length(head);
  printf("\n");
  printf(" Total clips: %d\n",n);
  printf("\n");
  print_lst(head);		/* prints the table */

  return 0;
}

struct clip *build_a_lst(char *fn) {
  FILE *fp;
  struct clip *hp;
  char *fields[MAX_FIELDS];
  char line[LINE_LENGTH];
  hp=NULL;

  fp = fopen(fn, "r");
  while (fgets(line, LINE_LENGTH, fp) != NULL) {
    split_line(&fields, line);
    hp = append(hp,&fields); 
  }

  return hp;
}

/* fields will have five values stored upon return */
void split_line(char **fields,char *line) {
  int i=0;
  char *token, *delim;
  delim = ",\n";
  
  token = strtok(line, delim);
  //printf("\n");

  while( token != NULL )
  {
   
    *fields++=token;
    token = strtok(NULL, delim);

    //printf("%s", token);
    
  } 
}

/* set four values into a clip, insert a clip at the of the list */
struct clip *append(struct clip *hp,char **fields) {
  struct clip *cp,*tp;
  //printf("%s\n",fields[0]);
  //printf("%s\n",fields[1]);
  //printf("%s\n",fields[2]);
  //printf("%s\n",fields[3]);
  //printf("%s\n",fields[4]);

  tp = (struct clip *) malloc(sizeof(struct clip));
  tp->views = atoi(fields[0]);

  tp->user = (char *) malloc(sizeof(char) * (strlen(fields[1])));
  tp->time = (char *) malloc(sizeof(char) * (strlen(fields[2])));
  tp->duration = (char *) malloc(sizeof(char) * (strlen(fields[3])));
  tp->title = (char *) malloc(sizeof(char) * (strlen(fields[4])));

  tp->next = NULL;

  strcpy(tp->user, fields[1]);
  strcpy(tp->time, fields[2]);
  strcpy(tp->duration, fields[3]);
  strcpy(tp->title, fields[4]);

  // Append to empty list
  if (!hp) {
    return tp;
  }

  cp = hp;
  while (cp->next) cp = cp->next;
  cp->next = tp;

  return hp;
}

void print_lst(struct clip *cp) {
  while (cp) {
     printf("%d,%s,%s,%s,%s\n",cp->views,cp->user,cp->duration,cp->title,cp->time);
     printf("\n");
     cp = cp->next;
  }
}

int find_length(struct clip *cp) {
  int length = 0;
  while (cp != NULL) {
    length++;
    cp = cp->next;
  }

  return length;
}



