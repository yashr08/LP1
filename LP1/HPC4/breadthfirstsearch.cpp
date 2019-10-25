#include<stdio.h>
#include<sys/time.h>
#include<stdlib.h>
#include<omp.h>
int q[10];
int qptr;
int visited[7];
int qfront;

void bfs(int adj_matrix[7][7],int nodecount,int lastnode)
{
	if(q[qfront]==lastnode)
	{
		printf("%d ---FOUND\n",q[qfront]);
		return;
	}
	else
	{
		#pragma omp parallel for
		for(int i=0;i<nodecount;i++)
		{
			if(adj_matrix[q[qfront]][i]==1&&visited[i]==0)
			{
				visited[i]=1;
				//printf("(%d added to queue by thread %d)",i,omp_get_thread_num());
				q[qptr++]=i;

			}
		}
	}
	printf("%d->",q[qfront]);
	qfront++;
	bfs(adj_matrix,nodecount,lastnode);
}

int main()
{
	int adj_matrix[7][7]={
		{0,  1  ,1  ,0  ,0  ,0  ,0},
		{1	,0	,1	,1	,0	,0	,0},
		{1	,1	,0	,0	,1	,0	,0},
		{0	,1	,0	,0	,1	,0	,0},
		{0	,0	,1	,1	,0	,1	,0},
		{0	,0	,0	,0	,1	,0	,1},
		{0	,0	,0	,0	,0	,1	,0}
	};
	int nodecount=7;
	int lastnode=0;
	int node_start=3;
	qptr=0;
	qfront=0;
	for(int i=0;i<7;i++)
		visited[i]=0;


	q[qptr++]=node_start;
	visited[node_start]=1;


	struct timeval starttime,endtime;

	gettimeofday(&starttime,NULL);

	bfs(adj_matrix,nodecount,lastnode);

	gettimeofday(&endtime,NULL);
}
