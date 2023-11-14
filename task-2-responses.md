**1. How closely does your approximation fit the actual solution? Is it closer on the left side or the right side of the graphs, or neither? Why or why not?**

My approximation was fairly accurate (R<sup>2</sup>=0.71), with diminishing accuracy as the graph attained higher x-values. Euler's method relies on previous data points to make the next prediction. As a result, estimation errors culminate as more estimations are made, resulting in increasingly poor accuracy. Thus, predictions were more accurate on the left side, though the reverse would be true if the steps were negative.

**2. Does the graph of the approximation get further away from the true graph at some points compared to others? If not, explain why not. If so, describe the shape of the graph where it is closer, and the shape of the graph when it is further away, then explain why you believe this is happening.**

Where concavity remains constant, error will accumulate along a trend. However, when concavity changes, that trend in error will temporarily counteract the error now trending in the opposite direction. As a result, the graph becomes most accurate before/after inflection points and least accurate before/after local extrema. Because Euler's Method uses a non-zero sampling interval, points of highest/lowest accuracy will rarely occur exactly on an inflection or extrema point, instead occuring immediately around them. Thus, the shape of the graph in high accuracy areas is relatively flat (concavity changes), while in low accuracy areas, it is rounded (attains extremum value). High/low accuracies areas are described as relative to adjacent accuracies (they are not universal).

**3. Now copy the code below the results for the approximation and the true solution and change the value of n to 201. Rerun the code. What changes do you observe when comparing the approximate solution to the true solution? Is this a better approximation or a worse approximation? Why?**

The approximate solution decreases in accuracy at a slower rate for n=201 than n=101. The overall accuracy is also improved (R<sup>2</sup>=0.91). By increasing the number of subintervals, the accuracy of each individual interval is increased. This results in lower error accumulation, thereby contributing to a better approximation. 

**4. What do you think would happen if you changed the value of n to 401? To 501?**

I think the rate at which performance decreases will decrease as n increases, and I think performance overall will increase (implying higher R<sup>2</sup> and lower RMSE/NRMSE). When actually tested, Root Mean Squared Error (RMSE) and Normalized Root Mean Squared Error (NRMSE) appear to decrease exponentially, indicating decreasingly improved performance as n increases. Thus, the performance will increase for n=401, and slightly more for n=501.
