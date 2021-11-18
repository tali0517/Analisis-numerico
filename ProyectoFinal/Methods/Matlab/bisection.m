%Bisection Method  
%Finds the root (f(x)=0) of a determined function 'f' in a specific
%interval
%Devolped by: Santiago Alzate, Sebastian Urrego, Esteban Sierra y Alejandro Castaño 
%Updated Last: 02/10/2021

%Input: 
%func = continous function 
%xmin, xmax = endpoints for the interval on func 
%tol = tolerance 
%sc = number of subintervals (Subinterval Count), defaults to 50

%Output: 
%x = Solution 
%icount = number of iterations 
%err = error

function [x, icount, err] = bisection(func,xmin, xmax, tol, sc)
if func(xmin) == 0
    disp('Lower endpoint of the function is one of the roots')
    return 
elseif func(xmax) == 0
    disp('Upper endpoint of the function is one of the roots')
    return
end

icount = 1 ;
err = 1000;
fmin = func(xmin);
th = (xmin+xmax)/2
fth = func(th);

while fth ~= 0 && err>tol && icount<sc     
    if sign(fmin) ~= sign(fth)
        tmax = th;
    else 
        tmin = th;
    end
    temp = th;
    th = (tmax+tmin)/2;
    fth = func(th);
    E = abs(th-temp);
    icount = icount+1
end

if th == 0
fprintf('Solution: %t is root', th)
else
    if E<tol
        fprint('%t is an approximation of a root with a tolerance of %v',th,tol)
    else
        fprintf('Failure after %g iterations', icount)
    end
end
    
    