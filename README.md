# K12-Physics-S2_SY2223

A collection of formulas for Physics calculations

* Hardcover - [Physics: Problems and Solutions](https://www.amazon.com/gp/product/1601530552/)

## References

* [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html)

## 1: Momentum

### 1.01: Semester Introduction

![image_1](1%20-%20Momentum/1-01%20-%20Semester%20Introduction/image_1.png)

### 1.02: Linear Momentum and Impulse

![image_1](1%20-%20Momentum/1-02%20-%20Linear%20Momentum%20and%20Impulse/image_1.png)

![image_2](1%20-%20Momentum/1-02%20-%20Linear%20Momentum%20and%20Impulse/image_2.png)

![image_3](1%20-%20Momentum/1-02%20-%20Linear%20Momentum%20and%20Impulse/image_3.png)

---

1. Suppose a 1,650 kg car is traveling at 15.0 m/s. Find the average force that is needed to stop the car in 4.0 s.

* What information are you given?

```js
// D is capital delta (Δ)
m = 1,650 kg
vi = 15.0 m/s
Dt = 4.0 s
```

* Find the initial momentum and final momentum.

```js
// D is capital delta (Δ)
// pi = m*v
let m = 1650; // kg
let v = 15.0; // m/s
let pi = m * v; // kg * m / s
console.log('pi =', pi, 'kg * m / s');
// pi = 24750 kg * m / s
let pf = 0; // kg * m / s
console.log('pf =', pf, 'kg * m / s');
// pf = 0 kg * m / s
let Dp = pf - pi; // kg * m / s
console.log('Dp =', Dp, 'kg * m / s');
// Dp = -24750 kg * m / s
```

* Use the impulse-momentum theorem to solve for the force and round to the correct number of significant figures.

```js
// D is capital delta (Δ)
let m = 1650; // kg
let v = 15.0; // m/s
let pi = m * v; // kg * m / s
let pf = 0; // kg * m / s
let Dp = pf - pi; // kg * m / s
let Dt = 4.0; // s
// F * Dt = Dp
// F = Dp / Dt
let F = Dp / Dt; // N
console.log('F =', F, 'N')
// F = -6187.5 N
console.log('F =', Math.round(F / Math.pow(10, 2)) * Math.pow(10, 2), 'N')
// F = -6200 N
```

---

2. A baseball with a mass of 0.145 kg approaches a bat at 45 m/s. After the bat hits the ball, the ball leaves the bat moving in the opposite direction at 50.0 m/s. Find the impulse and, using the force vs. time graph, the average force exerted by the bat. The time of the impulse can be determined from the graph. Dt = 0.001 s

* What information are you given?

```js
m = 0.145 kg
vi = 45 m/s
vf = −50.0 m/s
Dt = 0.001 s
```

* Write equations for the initial and final momenta.

```
p = m * v
pi = m * vi
pf = m * vf
```

* Solve for initial and final momenta.

```js
// D is capital delta (Δ)
let m = 0.145; // kg
let vi = 45; // m/s
let vf = -50.0; // m/s
let pi = m * vi; // kg * m / s
console.log('pi =', pi, 'kg * m / s');
// pi = 6.5249999999999995 kg * m / s
let pf = m * vf; // kg * m / s
console.log('pf =', pf, 'kg * m / s');
// pf = -7.249999999999999 kg * m / s
let Dp = pf - pi; // kg * m / s
console.log('Dp =', Dp, 'kg * m / s');
// Dp = -13.774999999999999 kg * m / s
console.log('impulse = Dp =', Math.round(Dp * Math.pow(10, 3)) / Math.pow(10, 3), 'kg * m / s');
// impulse = Dp = -13.775 kg * m / s
console.log('impulse = Dp =', Math.round(Dp), 'kg * m / s');
// impulse = Dp = -14 kg * m / s
```

* Find the average force.

```js
let m = 0.145; // kg
let vi = 45; // m/s
let vf = -50.0; // m/s
let pi = m * vi; // kg * m / s
let pf = m * vf; // kg * m / s
let Dp = pf - pi; // kg * m / s
let Dt = 0.001; // s
// F * Dt = Dp
// F = Dp / Dt
let F = Dp / Dt; // N
console.log('F =', F, 'N')
// F = -13774.999999999998 N
console.log('F =', Math.round(F / Math.pow(10, 3)) * Math.pow(10, 3), 'N')
// F = -14000 N
```
---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 38

### 1.03: Law of Conservation of Momentum

![image_1](/1%20-%20Momentum/1-03%20-%20Law%20of%20Conservation%20of%20Momentum/image_1.png)

```
pi == pf
```

---

1. An 8,500 kg train car moves at 12.0 m/s until it bumps into a stationary 8,500 kg car and latches onto it. What is the speed of the two cars linked together?

* What information is known?

```
m1 = 8500 kg
m2 = 8500 kg
Vi = 12.0 m/s
Vf = ? m/s
```
* Write what you know in equation form.

```
initial momentum = final momentum, or total pf = total pi
(m1 + m2) * Vf = m1 * Vi
Vf = (m1 / (m1 + m2)) * Vi
```

* Substitute and solve for final velocity.

```js
let m1 = 8500; // kg
let m2 = 8500; // kg
let Vi = 12.0; // m/s
let Vf = (m1/(m1+m2)) * Vi; // m/s
console.log('Vf =', Vf, 'm/s');
// Vf = 6 m/s
```

---

2. An astronaut adrift in space with no velocity throws a 38 kg wrench at13 m/s. The mass of the astronaut with the remaining equipment is165 kg. Find the velocity of the astronaut after she releases the wrench.

* What information is known?

```
Mass Wrench = Mw = 38 kg
Mass Astronaut = Ma = 165 kg
Vi = 0 m/s
Velocity Wrench = Vw = 13 m/s
Velocity Astronaut = Va = ?
```

* Find the astronaut’s final momentum.

```js
let Mw = 38; // kg
let Ma = 165; // kg
let Vw = 13; // m/s
// total momentum = pt
// pa = momentum of astronaut
// pw = momentum of wrench
// pt = pa + pw
// 0 = (Ma * Va) + (Mw * Vw)
let Va = -Mw * Vw / Ma; // m/s
console.log('Va =', Va, 'm/s');
// -2.993939393939394 m/s
console.log('Va =', Math.round(Va), 'm/s');
// Va = -3 m/s
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 39
