%Fake rule Method 
%This method is used to find the solution for equation f(x)= 0 on a set interval [xmin,xmax]

%Input:
%func = continuous function 
%xmin,xmax = Upper and lower bounds for said function 
%tol = tolerance 
%sc = subinterval count 

%Output:
%Z matrix with data for every iteration [iteration#, lower bound,
%upperbound, intermediate value, func's return for int. value, and error. 

function fp = falsePosition(func, xmin, xmax, tol, sc)
fmax = func(xmax);
fmin = func(xmin);
icount = 1;
error = 1000; 
th = (xmin)-((func(xmin)*(xmin-xmax))/(func(xmax)-f(xmin)));
fth = func(th);
Z = [icount, xmin, xmax,th,fth,error];

while error > tol 
    if sign(fth) == sign(fmax)
        xmax = th;
        fmax = fth;
    else
        xmin = th;
        fmin = fth;
    end 
    temp = th; 
    th = (xmin)-((func(xmin)*(xmin-xmax))/(func(xmax)-f(xmin)));
    fth = func(th);
    error = abs(th-temp)/th;
    icount = icount+1;
    Z(icount,1)= icount;
    Z(icount,2)=xmin;
    Z(icount,3)=xmax;
    Z(icount,4)=th;
    Z(icount,5)=fth;
    Z(icount,6)=error;
end
if fth==0
disp('SOLUTION:%g is root',th);
else
if Error<Tol
disp('SOLUTION:%g is an approximation to a root with a tolerance %f',th,tol);
else
disp('SOLUTION: Failure after %g iterations',icount);
end
end
end
