%Fixed Point  
%Finds the root (f(x)=0) of a determined function solving an analogous
%function x=g(x), through the fixed point method. 
%Devolped by: Santiago Alzate, Sebastian Urrego, Esteban Sierra y Alejandro Castaño 
%Updated Last: 03/10/2021

%Input: 
%func = continous function 
%gunc = continous function 
%startp = starting point 
%tol = tolerance 
%sc = number of subintervals (Subinterval Count), defaults to 50

%Output: 
%x = Solution 
%icount = number of iterations 
%err = error

function [x, icount, err] = fixedPoint(gunc, startp, tol)
x1=startp;
x2=gunc(x1);
icount = 1;

while abs(x2-x1) > tol
    x1 = x2; ;
    x2=gunc(x1);
    err = abs((x1-startp)/x1);
    icount = icount + 1;
end

if x2==0
disp('SOLUTION:%g is root',startp);
else
if Error<Tol
disp('SOLUTION:%g is an approximation with a tolerance of %f',startp,tol);
else
disp('SOLUTION: Failure in %g iterations',icount);
end
end