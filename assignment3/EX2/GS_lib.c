void gauss_seidel(double **newf,int n1,int n0){
    int  i,j;
    for (i=1;i<n1-1;i++){
    
    	for(j=1;j<n0-1;j++){
        
            newf[i][j] = 0.25 * (newf[i][j+1] + newf[i][j-1] +
                                   newf[i+1][j] + newf[i-1][j]);
           }
    }
}
