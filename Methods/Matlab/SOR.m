%Program to find solution to linear system Ax=b, 
% with SOR method. 

%Input:
%A: Invertible matrix 
%b: constant vector 
%startp = Initial approximation
%pondf = ponderation factor 
%tol = tolerance
%iMax = iteration cap 

function [x,iter,err] = SOR(A,b,startp,pondf,tol,iMax)

D = diag(diag(A));
L = -tril(A)+D;
U = -triu(A)+D;
T=inv(D-pondf*L)*((1-pondf)*D+pondf*U);
C=pondf*inv(D-w*L)*b;
prevx = startp;
E = 1000; 
iter = 0;

while E>tol && cont<iMax
    currx = T*prevx+C;
    E = norm(prevx-currx);
    prevx = currx;
    iter = iter + 1
    disp('Iteration %d: %f with error: %f',iter, currx, E);
end
disp('Method finished with an error of %f, with the final approximation: %f',E,currx);

x = currx;
c = iter; 
err = E; 
end