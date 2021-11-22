%Incremental Search 
%Finds sign changes in a determined interval [xmin,xmax] of function f(x)
%Devolped by: Santiago Alzate, Sebastian Urrego, Esteban Sierra y Alejandro Castaño 
%Updated Last: 02/10/2021

%Input: 
%func = continous function 
%x0 = starting estimate  
%sc = number of subintervals (Subinterval Count), defaults to 50


%Output: 
%lb = Lower bound/Left bound for the interval 
%ul = Upper bound/Right bound for the interval
%icount = number of iterations 

function xv = incSearch(func, x0, sc)
if nargin < 3, error('At least 3 arguments are required for this function'), end 
if nargin <4, sc = 50; end 
x = linspace(xmin, xmac, sc); 
f = func(x);
nv = 0  %Number of valuable brackets (where  there is a sign change) 
xv = [] %Base of the return value, no sign changes = empty vector return. 

for k = 1:length(x)-1
    if sign(f(k)) ~= sign(f(k+1))
        nv = nv + 1;
        xv(nv,1) = x(k);
        xv(nv,2) = x(k+1);
    end
end
if isempty(xv)
    disp('No brackets with sign change found')
else
    disp('Number of brackets: ')
    disp(nv)
end
    