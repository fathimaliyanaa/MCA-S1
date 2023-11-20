include<stdio.h>
int main()
{
        int i,j,k,n1,n2;
        int arr1[100],arr2[100],arr3[100];
        printf("Enter the size of first array:");
        scanf("%d",&n1);
        printf("\nEnter the size of second array:");
        scanf("%d",&n2);
        for(i=0;i<n1;i++)
        {
                scanf("%d",&arr1[i]);

        }
        printf("Enter the number of elements in second array : ");

        for(i=0;i<n2;i++)
        {
                scanf("%d",&arr2[i]);
        }
        i=0;
        j=0;
        k=0;
        while(i<n1 && j<n2)
                {
                        if(arr1[i]<arr2[j])
                        {
                                arr3[k++] = arr1[i];
                                i++;
                        }
                        else{
                                arr3[k++] = arr2[j];
                                j++;
                        }
                }
        while(i<n1)
                {
                        arr3[k++]=arr1[i];
                        i++;
                }
        while(j<n2)
                {
                        arr3[k++]=arr2[j];
                        j++;
                }
        printf("Elements of array 3 in sorted order:");
        for(i=0;i<n1+n2;i++)
                {
                        printf("%d\t",arr3[i]);
                }
return 0;
