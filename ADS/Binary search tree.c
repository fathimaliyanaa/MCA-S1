#include&lt;stdio.h&gt;
#include&lt;stdlib.h&gt;

struct node{
int data;
struct node *left_child;
struct node *right_child;
};

struct node* new_node(int x){
struct node *p;
p = malloc(sizeof(struct node));
p-&gt;data = x;
p-&gt;left_child = NULL;
p-&gt;right_child = NULL;
return p;
}

struct node* insert(struct node* root,int x){
if(root==NULL){
return new_node(x);
}
else if(x &gt; root-&gt;data){
root-&gt;right_child = insert(root-&gt;right_child,x);
}
else{

root-&gt;left_child = insert(root-&gt;left_child,x);
}
return root;
}

struct node* search(struct node* root,int x){
if(root==NULL){
printf(&quot;Value is not there\n&quot;);
}
else if(root-&gt;data==x){
printf(&quot;Value is there\n&quot;);
}
else if(x &gt; root-&gt;data){
return search(root-&gt;right_child,x);
}
else{
return search(root-&gt;left_child,x);
}
}

struct node* Findmin(struct node* root){
if (root-&gt;left_child != NULL){
return Findmin(root-&gt;left_child);
}
else{
return root;
}
}

struct node* Delete(struct node *root, int x)
{

if(root==NULL)
return NULL;
if (x&gt;root-&gt;data)
root-&gt;right_child = Delete(root-&gt;right_child, x);
else if(x&lt;root-&gt;data)
root-&gt;left_child = Delete(root-&gt;left_child, x);
else
{
if(root-&gt;left_child==NULL &amp;&amp; root-&gt;right_child==NULL)
{
free(root);
}

else if(root-&gt;left_child==NULL || root-&gt;right_child==NULL)
{
struct node *temp;
if(root-&gt;left_child==NULL)
temp = root-&gt;right_child;
else
temp = root-&gt;left_child;
free(root);
return temp;
}

else{
struct node *temp =Findmin(root-&gt;right_child);
root-&gt;data = temp-&gt;data;
root-&gt;right_child=Delete(root-&gt;right_child, temp-&gt;data);
}
}

return root;
}

void printtree(struct node *root)
{
if(root!=NULL)
{
printtree(root-&gt;left_child);
printf(&quot; %d &quot;, root-&gt;data);
printtree(root-&gt;right_child);
}
}

int main(){
int option,val;
struct node* root=NULL;
printf(&quot;\n*********************Options**********************\n&quot;);
printf(&quot;1)Insert a new node\n&quot;);
printf(&quot;2)Search a value from binary tree\n&quot;);
printf(&quot;3)Delete a node\n&quot;);

printf(&quot;4)Print the binary tree\n&quot;);
printf(&quot;5)Exit&quot;);

do{
printf(&quot;\nEnter the option : &quot;);
scanf(&quot;%d&quot;,&amp;option);
switch(option){
case 1: printf(&quot;Enter the value you want to insert : &quot;);

scanf(&quot;%d&quot;,&amp;val);
root = insert(root,val);
printf(&quot;Value inserted\n&quot;);
break;

case 2: printf(&quot;Enter the value you want to search : &quot;);

scanf(&quot;%d&quot;,&amp;val);
search(root,val);
break;

case 3: printf(&quot;Enter the value you want to delete : &quot;);

scanf(&quot;%d&quot;,&amp;val);
root = Delete(root,val);
printf(&quot;Node is deleted&quot;);
break;

case 4: printtree(root);
break;
case 5: printf(&quot;EXIT&quot;);
exit(0);

default: printf(&quot;Incorrect option. Please try again\n&quot;);
}
}while(option != 6);

}
