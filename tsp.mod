param n > 0 integer;
param d{1..n,1..n} >= 0;
var x{1..n,1..n} binary;
var u{2..n} >= 0 integer ;
var z >=0 ;

minimize custo: sum{i in 1..n,j in 1..n:i<>j}d[i,j]* x[i,j];

subject to r1{j in 1..n}: sum{i in 1..n: i<>j}x[i,j] = 1;
subject to r2{i in 1..n}: sum{j in 1..n:j<>i}x[i,j] = 1;

subject to r3{i in 2..n,j in 2..n:i<>j}: u[i] - u[j] +(n-1)*x[i,j]<= n - 2;
subject to r4{i in 2..n}: 1<= u[i] <= n - 1;
