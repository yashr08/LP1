Breadthfs is not complete

int omp_get_thread_num(); (to get running thread no)
#pragma omp parallel for ( to convert into parallel add this before for loop)
int iCPU = omp_get_num_procs(); ( to get no of processors)
omp_set_num_threads(iCPU); ( setting no of threads)

g++ -fopenmp code.cpp
./a.out
