# K12-Physics-S2_SY2223

A collection of formulas for Physics calculations

* Hardcover - [Physics: Problems and Solutions](https://www.amazon.com/gp/product/1601530552/)

## References

* [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html)

## Chapters

* [Chapters 1 - 5](Chapters_1_5.md)

* [Chapters 6 - 10](Chapters_6_10.md)

---

## 6: Light

---

### 6.01: The Electromagnetic Spectrum

---

![image_1](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_1.png)

![image_2](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_2.png)

![image_3](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_3.png)

![image_4](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_4.png)

![image_5](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_5.png)

![image_6](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_6.png)

![image_7](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_7.png)

![image_8](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_8.png)

![image_9](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_9.png)

![image_10](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_10.png)

![image_11](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_11.png)

![image_12](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_12.png)

![image_13](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_13.png)

![image_14](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_14.png)

![image_15](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_15.png)

![image_16](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_16.png)

![image_17](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_17.png)

![image_18](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_18.png)

![image_19](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_19.png)

![image_20](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_20.png)

![image_21](6%20-%20Light/6-01%20-%20The%20Electromagnetic%20Spectrum/image_21.png)

---

1. Light from a particular source has a wavelength of 480 nm.
Find the frequency f of the light.

```js
const c = 3.0 * Math.pow(10, 8); // m/s
let wavelength = 480 * Math.pow(10, -9); // m
let f = c / wavelength; // Hz
console.log('f =', f.toExponential(), 'Hz');
// f = 6.249999999999999e+14 Hz
console.log('f =', Number(f.toPrecision(2)).toExponential(), 'Hz');
// f = 6.2e+14 Hz
```

---

2. Light from a particular source has a wavelength of 500 nm.
Find the frequency f of the light.

```js
const c = 3.0 * Math.pow(10, 8); // m/s
let wavelength = 500 * Math.pow(10, -9); // m
let f = c / wavelength; // Hz
console.log('f =', f.toExponential(), 'Hz');
// f = 5.999999999999999e+14 Hz
console.log('f =', Number(f.toPrecision(2)).toExponential(), 'Hz');
// f = 6e+14 Hz
```

---

3. Light from a particular source has a frequency of 6.0 x 10^14 Hz. Find the wavelength of the light.

```js
const c = 3.0 * Math.pow(10, 8); // m/s
let f = 6.0 * Math.pow(10, 14); // Hz
let wavelength = c / f; // m
console.log('wavelength =', wavelength.toExponential(), 'm');
// wavelength = 5e-7 m
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 61

---

### 6.02: Diffraction and Interference

---

![image_1](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_1.png)

![image_2](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_2.png)

![image_3](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_3.png)

![image_4](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_4.png)

![image_5](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_5.png)

![image_6](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_6.png)

![image_7](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_7.png)

![image_8](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_8.png)

![image_9](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_9.png)

![image_10](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_10.png)

![image_11](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_11.png)

![image_12](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_12.png)

![image_13](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_13.png)

![image_14](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_14.png)

![image_15](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_15.png)

![image_16](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_16.png)

![image_17](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_17.png)

![image_18](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_18.png)

![image_19](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_19.png)

![image_20](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_20.png)

![image_21](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_21.png)

![image_22](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_22.png)

![image_23](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_23.png)

![image_24](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_24.png)

![image_25](6%20-%20Light/6-02%20-%20Diffraction%20and%20Interference/image_25.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 62

---

### 6.03: Reflection

---

![image_1](6%20-%20Light/6-03%20-%20Reflection/image_1.png)

![image_2](6%20-%20Light/6-03%20-%20Reflection/image_2.png)

![image_3](6%20-%20Light/6-03%20-%20Reflection/image_3.png)

![image_4](6%20-%20Light/6-03%20-%20Reflection/image_4.png)

![image_5](6%20-%20Light/6-03%20-%20Reflection/image_5.png)

![image_6](6%20-%20Light/6-03%20-%20Reflection/image_6.png)

![image_7](6%20-%20Light/6-03%20-%20Reflection/image_7.png)

![image_8](6%20-%20Light/6-03%20-%20Reflection/image_8.png)

![image_9](6%20-%20Light/6-03%20-%20Reflection/image_9.png)

![image_10](6%20-%20Light/6-03%20-%20Reflection/image_10.png)

![image_11](6%20-%20Light/6-03%20-%20Reflection/image_11.png)

![image_12](6%20-%20Light/6-03%20-%20Reflection/image_12.png)

![image_13](6%20-%20Light/6-03%20-%20Reflection/image_13.png)

![image_14](6%20-%20Light/6-03%20-%20Reflection/image_14.png)

![image_15](6%20-%20Light/6-03%20-%20Reflection/image_15.png)

![image_16](6%20-%20Light/6-03%20-%20Reflection/image_16.png)

![image_17](6%20-%20Light/6-03%20-%20Reflection/image_17.png)

![image_18](6%20-%20Light/6-03%20-%20Reflection/image_18.png)

![image_19](6%20-%20Light/6-03%20-%20Reflection/image_19.png)

![image_20](6%20-%20Light/6-03%20-%20Reflection/image_20.png)

---

1. Flint glass has an index of refraction n = 1.66. What is the critical angle for light in the glass?

```js
const refraction_air = 1;
const refraction_glass = 1.66;
// sin(theta) = 1/1.66
let ratio = refraction_air / refraction_glass;
console.log('ratio =', ratio);
// ratio = 0.6024096385542169
console.log('ratio =', ratio.toPrecision(3));
// ratio = 0.602
let angle = Math.asin(ratio) * 180 / Math.PI; // degrees
console.log('angle =', angle, 'degrees');
// angle = 37.08506032429864 degrees
console.log('angle =', Math.round(angle), 'degrees');
// angle = 37 degrees
```

---

2. What is the index of refraction when the critical angle for light is 37 degrees?

```js
const refraction_air = 1;
const angle = 37; // degrees
let ratio = Math.sin(angle / 180 * Math.PI); // refraction index
console.log('ratio =', ratio);
let index = refraction_air / ratio;
console.log('index =', index, 'refraction index');
// index = 1.6616401411224833 refraction index
console.log('index =', index.toPrecision(3), 'refraction index');
// index = 1.66 refraction index
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 63

---

### 6.04: Refraction

---

![image_1](6%20-%20Light/6-04%20-%20Refraction/image_1.png)

![image_2](6%20-%20Light/6-04%20-%20Refraction/image_2.png)

![image_3](6%20-%20Light/6-04%20-%20Refraction/image_3.png)

![image_4](6%20-%20Light/6-04%20-%20Refraction/image_4.png)

![image_5](6%20-%20Light/6-04%20-%20Refraction/image_5.png)

![image_6](6%20-%20Light/6-04%20-%20Refraction/image_6.png)

![image_7](6%20-%20Light/6-04%20-%20Refraction/image_7.png)

![image_8](6%20-%20Light/6-04%20-%20Refraction/image_8.png)

![image_9](6%20-%20Light/6-04%20-%20Refraction/image_9.png)

![image_10](6%20-%20Light/6-04%20-%20Refraction/image_10.png)

![image_11](6%20-%20Light/6-04%20-%20Refraction/image_11.jpg)

![image_12](6%20-%20Light/6-04%20-%20Refraction/image_12.png)

![image_13](6%20-%20Light/6-04%20-%20Refraction/image_13.png)

![image_14](6%20-%20Light/6-04%20-%20Refraction/image_14.png)

![image_15](6%20-%20Light/6-04%20-%20Refraction/image_15.png)

![image_16](6%20-%20Light/6-04%20-%20Refraction/image_16.png)

![image_17](6%20-%20Light/6-04%20-%20Refraction/image_17.png)

![image_18](6%20-%20Light/6-04%20-%20Refraction/image_18.png)

---

1. Light with a wavelength of 580 nm enters water, which has an index of refraction of 1.33. Find the wavelength of the light in water.

```js
const wavelengthAir = 580 * Math.pow(10, -9); // m
const indexWater = 1.33;
let wavelengthWater = wavelengthAir / indexWater; // m
console.log('wavelengthWater =', wavelengthWater.toExponential(), 'm');
// wavelengthWater = 4.360902255639098e-7 m
console.log('wavelengthWater =', Number(wavelengthWater.toPrecision(3)).toExponential(), 'm');
// wavelengthWater = 4.36e-7 m
```

---

2. Show that it follows from Snell’s law that light bends toward the normal when it enters a medium with a higher refractive index and away from the normal when it enters a medium with a lower refractive index.

```js
// Light bends toward the normal surface when it enters a medium with a higher refractive index.
// Light bends away from the normal when it enters a medium with a lower refractive index.
//
// n1 * sin(A) = n2 * sin(B)
//
function calculateCriticalAngle(n1, n2) {
  const min = Math.min(n1, n2);
  const max = Math.max(n1, n2);
  let ratio = n1 / n2;
  let angle = Math.asin(min/max) * 180 / Math.PI; // degrees
  if (n1 > n2) {
    angle = -angle;
  }
  console.log('n1=', n1, 'n2=', n2, 'ratio =', ratio.toPrecision(3), 'angle=', Math.round(angle));
}

const index_air = 1.003;
const index_acrylic_glass = 1.5;
const index_flint_glass = 1.62;

console.log('n1 == n2:');
calculateCriticalAngle(index_air, index_air);
// n1= 1.003 n2= 1.003 ratio = 1.00 angle= 90
calculateCriticalAngle(index_acrylic_glass, index_acrylic_glass);
// n1= 1.5 n2= 1.5 ratio = 1.00 angle= 90
calculateCriticalAngle(index_flint_glass, index_flint_glass);
// n1= 1.62 n2= 1.62 ratio = 1.00 angle= 90

console.log('n1 < n2:');
calculateCriticalAngle(index_air, index_acrylic_glass);
// n1= 1.003 n2= 1.5 ratio = 0.669 angle= 42
calculateCriticalAngle(index_air, index_flint_glass);
// n1= 1.003 n2= 1.62 ratio = 0.619 angle= 38
calculateCriticalAngle(index_acrylic_glass, index_flint_glass);
// n1= 1.5 n2= 1.62 ratio = 0.926 angle= 68

console.log('n1 > n2:');
calculateCriticalAngle(index_acrylic_glass, index_air);
// n1= 1.5 n2= 1.003 ratio = 1.50 angle= -42
calculateCriticalAngle(index_flint_glass, index_air);
// n1= 1.62 n2= 1.003 ratio = 1.62 angle= -38
calculateCriticalAngle(index_flint_glass, index_acrylic_glass);
// n1= 1.62 n2= 1.5 ratio = 1.08 angle= -68
```

---

3. Suppose a beam of light enters a plate of crown glass at an angle of incidence of 30°. Find its angle of refraction.

```js
// n1 * sin(A) = n2 * sin(B)
function calculateRefractionAngle(n1, n2, deg1) {
  const min = Math.min(n1, n2);
  const max = Math.max(n1, n2);
  const rad1 = deg1 / 180 * Math.PI; // radians
  let ratio = min / max * Math.sin(rad1);
  let rad2 = Math.asin(ratio); // radians
  if (n1 > n2) {
    rad2 = -rad2;
  }
  let deg2 = rad2 * 180 / Math.PI; // degrees
  console.log('n1=', n1, 'n2=', n2, 'ratio =', ratio.toPrecision(3), 'deg1=', Math.round(deg1), 'deg2=', deg2.toPrecision(3));
}

const index_air = 1.003;
const index_crown_glass = 1.52;
const angle = 30; // degrees

calculateRefractionAngle(index_air, index_crown_glass, angle);
// n1= 1.003 n2= 1.52 ratio = 0.330 deg1= 30 deg2= 19.3

// The angle of refraction, as expected, is smaller than the incident angle of 30°, and the light bends toward the normal in entering the denser (higher n) medium.
```

---

4. A flat transparent piece of acrylic is at the bottom of a beaker of water, A beam of light passes through the water to strike the acrylic at an angle of incidence of 35°. What angle does the beam make with the normal to the acrylic surface as it travels inside the acrylic?

```js
// n1 * sin(A) = n2 * sin(B)
function calculateRefractionAngle(n1, n2, deg1) {
  const min = Math.min(n1, n2);
  const max = Math.max(n1, n2);
  const rad1 = deg1 / 180 * Math.PI; // radians
  let ratio = min / max * Math.sin(rad1);
  let rad2 = Math.asin(ratio); // radians
  if (n1 > n2) {
    rad2 = -rad2;
  }
  let deg2 = rad2 * 180 / Math.PI; // degrees
  console.log('n1=', n1, 'n2=', n2, 'ratio =', ratio.toPrecision(3), 'deg1=', Math.round(deg1), 'deg2=', deg2.toPrecision(3));
}

const index_water = 1.33;
const index_acrylic_glass = 1.5;
const angle = 35; // degrees

calculateRefractionAngle(index_water, index_acrylic_glass, angle);
// n1= 1.33 n2= 1.5 ratio = 0.509 deg1= 35 deg2= 30.6

// The beam of light is bent closer to the normal because it goes from a region of lower index of refraction to a region with a higher index of refraction.
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 64

---

### 6.05 Mirrors

---

![image_1](6%20-%20Light/6-05%20-%20Mirrors/image_1.png)

![image_2](6%20-%20Light/6-05%20-%20Mirrors/image_2.png)

![image_3](6%20-%20Light/6-05%20-%20Mirrors/image_3.png)

![image_4](6%20-%20Light/6-05%20-%20Mirrors/image_4.png)

![image_5](6%20-%20Light/6-05%20-%20Mirrors/image_5.png)

![image_6](6%20-%20Light/6-05%20-%20Mirrors/image_6.png)

![image_7](6%20-%20Light/6-05%20-%20Mirrors/image_7.png)

![image_8](6%20-%20Light/6-05%20-%20Mirrors/image_8.png)

![image_9](6%20-%20Light/6-05%20-%20Mirrors/image_9.png)

![image_10](6%20-%20Light/6-05%20-%20Mirrors/image_10.png)

![image_11](6%20-%20Light/6-05%20-%20Mirrors/image_11.png)

![image_12](6%20-%20Light/6-05%20-%20Mirrors/image_12.png)

![image_13](6%20-%20Light/6-05%20-%20Mirrors/image_13.png)

![image_14](6%20-%20Light/6-05%20-%20Mirrors/image_14.png)

![image_15](6%20-%20Light/6-05%20-%20Mirrors/image_15.png)

![image_16](6%20-%20Light/6-05%20-%20Mirrors/image_16.png)

![image_17](6%20-%20Light/6-05%20-%20Mirrors/image_17.png)

![image_18](6%20-%20Light/6-05%20-%20Mirrors/image_18.png)

![image_19](6%20-%20Light/6-05%20-%20Mirrors/image_19.png)

![image_20](6%20-%20Light/6-05%20-%20Mirrors/image_20.png)

![image_21](6%20-%20Light/6-05%20-%20Mirrors/image_21.png)

![image_22](6%20-%20Light/6-05%20-%20Mirrors/image_22.png)

![image_23](6%20-%20Light/6-05%20-%20Mirrors/image_23.png)

![image_24](6%20-%20Light/6-05%20-%20Mirrors/image_24.png)

![image_25](6%20-%20Light/6-05%20-%20Mirrors/image_25.png)

![image_26](6%20-%20Light/6-05%20-%20Mirrors/image_26.png)

![image_27](6%20-%20Light/6-05%20-%20Mirrors/image_27.png)

![image_28](6%20-%20Light/6-05%20-%20Mirrors/image_28.png)

![image_29](6%20-%20Light/6-05%20-%20Mirrors/image_29.png)

![image_30](6%20-%20Light/6-05%20-%20Mirrors/image_30.png)

![image_31](6%20-%20Light/6-05%20-%20Mirrors/image_31.png)

![image_32](6%20-%20Light/6-05%20-%20Mirrors/image_32.png)

![image_33](6%20-%20Light/6-05%20-%20Mirrors/image_33.png)

![image_34](6%20-%20Light/6-05%20-%20Mirrors/image_34.png)

---

1. What is the radius given the focal length of 25 mm?

```js
let focalLength = 0.025; // m
let radius = 2 * focalLength; // m
console.log('radius', radius, 'm');
// radius 0.05 m
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 65

---

## 6.06: Lenses

---

![image_1](6%20-%20Light/6-06%20-%20Lenses/image_1.png)

![image_2](6%20-%20Light/6-06%20-%20Lenses/image_2.png)

![image_3](6%20-%20Light/6-06%20-%20Lenses/image_3.png)

![image_4](6%20-%20Light/6-06%20-%20Lenses/image_4.png)

![image_5](6%20-%20Light/6-06%20-%20Lenses/image_5.png)

![image_6](6%20-%20Light/6-06%20-%20Lenses/image_6.png)

![image_7](6%20-%20Light/6-06%20-%20Lenses/image_7.png)

![image_8](6%20-%20Light/6-06%20-%20Lenses/image_8.png)

![image_9](6%20-%20Light/6-06%20-%20Lenses/image_9.png)

![image_10](6%20-%20Light/6-06%20-%20Lenses/image_10.png)

![image_11](6%20-%20Light/6-06%20-%20Lenses/image_11.png)

![image_12](6%20-%20Light/6-06%20-%20Lenses/image_12.png)

![image_13](6%20-%20Light/6-06%20-%20Lenses/image_13.png)

![image_14](6%20-%20Light/6-06%20-%20Lenses/image_14.png)

![image_15](6%20-%20Light/6-06%20-%20Lenses/image_15.png)

![image_16](6%20-%20Light/6-06%20-%20Lenses/image_16.png)

![image_17](6%20-%20Light/6-06%20-%20Lenses/image_17.png)

![image_18](6%20-%20Light/6-06%20-%20Lenses/image_18.png)

![image_19](6%20-%20Light/6-06%20-%20Lenses/image_19.png)

![image_20](6%20-%20Light/6-06%20-%20Lenses/image_20.png)

![image_21](6%20-%20Light/6-06%20-%20Lenses/image_21.png)

![image_22](6%20-%20Light/6-06%20-%20Lenses/image_22.png)

![image_23](6%20-%20Light/6-06%20-%20Lenses/image_23.png)

![image_24](6%20-%20Light/6-06%20-%20Lenses/image_24.png)

![image_25](6%20-%20Light/6-06%20-%20Lenses/image_25.png)

![image_26](6%20-%20Light/6-06%20-%20Lenses/image_26.png)

![image_27](6%20-%20Light/6-06%20-%20Lenses/image_27.png)

![image_28](6%20-%20Light/6-06%20-%20Lenses/image_28.png)

![image_29](6%20-%20Light/6-06%20-%20Lenses/image_29.png)

![image_30](6%20-%20Light/6-06%20-%20Lenses/image_30.png)

![image_31](6%20-%20Light/6-06%20-%20Lenses/image_31.png)

![image_32](6%20-%20Light/6-06%20-%20Lenses/image_32.png)

![image_33](6%20-%20Light/6-06%20-%20Lenses/image_33.png)

![image_34](6%20-%20Light/6-06%20-%20Lenses/image_34.png)

![image_35](6%20-%20Light/6-06%20-%20Lenses/image_35.png)

![image_36](6%20-%20Light/6-06%20-%20Lenses/image_36.png)

![image_37](6%20-%20Light/6-06%20-%20Lenses/image_37.png)

![image_38](6%20-%20Light/6-06%20-%20Lenses/image_38.png)

![image_39](6%20-%20Light/6-06%20-%20Lenses/image_39.png)

![image_40](6%20-%20Light/6-06%20-%20Lenses/image_40.png)

![image_41](6%20-%20Light/6-06%20-%20Lenses/image_41.png)

![image_42](6%20-%20Light/6-06%20-%20Lenses/image_42.png)

![image_43](6%20-%20Light/6-06%20-%20Lenses/image_43.png)

![image_44](6%20-%20Light/6-06%20-%20Lenses/image_44.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 66

---

## 7: Electric Forces

---

### 7.01: Static Electricity

---

![image_1](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_1.png)

![image_2](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_2.png)

![image_3](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_3.png)

![image_4](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_4.jpg)

![image_5](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_5.jpg)

![image_6](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_6.jpg)

![image_7](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_7.jpg)

![image_8](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_8.jpg)

![image_9](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_9.png)

![image_10](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_10.png)

![image_11](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_11.png)

![image_12](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_12.png)

![image_13](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_13.png)

![image_14](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_14.png)

![image_15](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_15.png)

![image_16](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_16.png)

![image_17](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_17.png)

![image_18](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_18.png)

![image_19](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_19.png)

![image_20](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_20.png)

![image_21](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_21.png)

![image_22](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_22.png)

![image_23](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_23.png)

![image_24](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_24.png)

![image_25](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_25.png)

![image_26](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_26.png)

![image_27](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_27.png)

![image_28](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_28.png)

![image_29](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_29.png)

![image_30](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_30.png)

![image_31](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_31.png)

![image_32](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_32.png)

![image_33](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_33.png)

![image_34](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_34.png)

![image_35](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_35.png)

![image_36](7%20-%20Electric%20Forces/7-01%20-%20Static%20Electricity/image_36.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 67

---

### 7.02: Electric Force

---

![image_1](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_1.png)

![image_2](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_2.png)

![image_3](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_3.png)

![image_4](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_4.png)

![image_5](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_5.png)

![image_6](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_6.png)

![image_7](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_7.png)

![image_8](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_8.png)

![image_9](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_9.png)

![image_10](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_10.png)

![image_11](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_11.png)

![image_12](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_12.png)

![image_13](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_13.png)

![image_14](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_14.png)

![image_15](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_15.png)

![image_16](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_16.png)

![image_17](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_17.png)

![image_18](7%20-%20Electric%20Forces/7-02%20-%20Electric%20Force/image_18.png)

---

```js
// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

//  Coulomb's law
F = k * q1 * q2 / Math.pow(r, 2);

// Newton’s Law of Universal Gravitation
F = G * m1 * m2 / Math.pow(r, 2);
```

* A charge of −1C negative 1 C is the equivalent of the electric force exerted by 6.24 x 10^18 electrons.

* A charge of +1C is the equivalent of 6.24 x 10^18 protons.

* One electron has a force of −1.6 × 10^-19 C

* One proton has a force of 1.6 × 10^-19 C

*  If two objects are 1 meter apart and each has a charge of +1 coulomb, the repelling force between them is an astounding 9 × 10^9 N, which is about 900,000 tons of force.

* A single lightning bolt has an electric charge ranging from 5 C to 10 C.

---

1. A negative charge of −2.0 x 10^−4 C
and a positive charge of +4.0 × 10^−4 C are separated by 0.20 m. What is the magnitude and direction of the force between them?

```js

let q1 = -2.0 * Math.pow(10, -4); // C
let q2 = 4.0 * Math.pow(10, -4); // C
let r = 0.2; // m

// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

//  Coulomb's law
let F = k * q1 * q2 / Math.pow(r, 2);
console.log('F =', F, 'N');
// F = -17999.999999999993 N
console.log('F =', F.toPrecision(2), 'N');
// F = -1.8e+4 N
```

* This is an attractive force as indicated by the fact that the value is negative.

---

2. What would happen if the distance was doubled?

```js
let q1 = -2.0 * Math.pow(10, -4); // C
let q2 = 4.0 * Math.pow(10, -4); // C
let r = 0.4; // m

// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

//  Coulomb's law
let F = k * q1 * q2 / Math.pow(r, 2);
console.log('F =', F, 'N');
// F = -4499.999999999998 N
console.log('F =', F.toPrecision(2), 'N');
// F = -4.5e+3 N
```

* This is an attractive force as indicated by the fact that the value is negative.

---

3. A charge of –2.0 × 10^–4 C and a charge of +4.0 × 10^–4 C are separated by 0.40 m. What is the magnitude and direction of the force between them?

```js
let q1 = -2.0 * Math.pow(10, -4); // C
let q2 = 4.0 * Math.pow(10, -4); // C
let r = 0.4; // m

// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

//  Coulomb's law
let F = k * q1 * q2 / Math.pow(r, 2);
console.log('F =', F, 'N');
// F = -4499.999999999998 N
console.log('F =', F.toPrecision(2), 'N');
// F = -4.5e+3 N
```

* Because the force is negative, the direction of the force is toward the other charge. You can confirm this by looking at the signs of the original charges. Because the two charges have opposite signs, they will attract each other.

---

4. Object A has a charge of +6.0 x 10^-6 C, while Object B has a charge of +3.0 x 10^-6 C. If the force between them is 1.8 x 10^2 N, then how far apart are they?

```js
let q1 = 6.0 * Math.pow(10, -6); // C
let q2 = 3.0 * Math.pow(10, -6); // C
let F = 1.8 * Math.pow(10, 2); // N

// Coulomb's constant
const k = 9.0 * Math.pow(10, 9); // N * m^2 / C^2

let r = Math.sqrt(k * q1 * q2 / F); // m
console.log('r =', r, 'm');
// r = 0.03 m
console.log('r =', r.toPrecision(2), 'm');
// r = 0.03 m
console.log('r =', r.toExponential(), 'm');
// r = 3e-2 m
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 68

---

### 7.03: Electric Fields

---

![image_1](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_1.png)

![image_2](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_2.png)

![image_3](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_3.png)

![image_4](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_4.png)

![image_5](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_5.png)

![image_6](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_6.png)

![image_7](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_7.png)

![image_8](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_8.png)

![image_9](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_9.png)

![image_10](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_10.png)

![image_11](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_11.png)

![image_12](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_12.png)

![image_13](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_13.png)

![image_14](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_14.png)

![image_15](7%20-%20Electric%20Forces/7-03%20-%20Electric%20Fields/image_15.png)

---

```js
// For a test charge q_prime
F = K * q_prime * Q / Math.pow(r, 2); // N

// strength of the field
E = F / q_prime; // N/C

// substition
E = K * Q / Math.pow(r, 2);
```

---

1. A positive test charge of 4.0 x 10^–6 C experiences a force of –0.060 N at an angle of 20° from a source charge. What is the strength and direction of the electric field?

```js
let q_prime = 4.0 * Math.pow(10, -6); // C
let F = -0.060; // N
let E = F / q_prime; // N/C
console.log('E =', E, 'N/C');
// E = -15000 N/C
console.log('E =', E.toPrecision(2), 'N/C');
// E = -1.5e+4 N/C
let originalAngle = 20; // degrees
let minAngle = 180; // degrees
let maxAngle = (180 + originalAngle) % 360; // degrees
console.log('minAngle =', minAngle, 'degrees');
// minAngle = 180 degrees
console.log('maxAngle =', maxAngle, 'degrees');
// maxAngle = 200 degrees
```

* When the force is negative, E is negative, which indicates that the direction of the field is inward and that the source charge is negative. The angle of the force would be 180° from the original angle, or 200°.

---

2. The strength of an electric field at 1.00 m from a source charge is –1.00 × 10^4 N/C. What is the magnitude of the source charge?

```js
let E = -1.00 * Math.pow(10, 4); // N/C
let r = 1.00; // m
let k = 9.00 * Math.pow(10, 9); // N*m^2/C^2
let Q = E * Math.pow(r, 2) / k; // C
console.log('Q =', Q.toExponential(), 'C');
// Q = -1.111111111111111e-6
console.log('Q =', Number(Q.toPrecision(3)).toExponential(), 'C');
// Q = -1.11e-6 C
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 69

---

### 7.07: Electric Potential Difference

---

![image_1](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_1.png)

![image_2](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_2.png)

![image_3](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_3.png)

![image_4](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_4.png)

![image_5](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_5.png)

![image_6](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_6.png)

![image_7](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_7.png)

![image_8](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_8.png)

![image_9](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_9.png)

![image_10](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_10.png)

![image_11](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_11.png)

![image_12](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_12.png)

![image_13](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_13.png)

![image_14](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_14.png)

![image_15](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_15.png)

![image_16](7%20-%20Electric%20Forces/7-07%20-%20Electric%20Potential%20Difference/image_16.png)

---

1. If an electric potential difference of 200.0 V occurs when a point charge of 1.0 μC is moved within an electric field, then what is the change in potential energy?

```js
let DV = 200.0; // V
let q = 1.0 * Math.pow(10, -6); // C
let DUe = q * DV; // J
console.log('DUe =', DUe.toExponential(), 'J');
// DUe = 1.9999999999999998e-4 J
console.log('DUe =', Number(DUe.toPrecision(2)).toExponential(), 'J');
// DUe = 2e-4 J
```

---

2. If 200.0 J of work is done to a point charge of 1.0 μC that is moved within an electric field, then what is the change in electric potential difference?

```js
let W = 200.0; // J
let q = 1.0 * Math.pow(10, -6); // C
let DV = W / q; // V
console.log('DV =', DV.toPrecision(2), 'V');
// DV = 2.0e+8 V
```

---

3. Two large parallel plates are 10.0 cm apart. The strength of the electric field between them is 500.0 N/C. What is the electric potential difference (ΔV) between them? How does this compare with the electric potential difference when the plates were 5.0 cm apart?

```js
let d = 0.10; // m
let E = 500.0; // N/C
let DV = E * d; // V
console.log('DV =', DV.toPrecision(2), 'V');
// DV = 50 V
```

```js
let d = 0.05; // m
let E = 500.0; // N/C
let DV = E * d; // V
console.log('DV =', DV.toPrecision(2), 'V');
// DV = 25 V
```

* ΔV doubled compared to when the plates were 5.0 cm apart.

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 70

---

## 8: Currents and Circuits

---

### 8.01: Currents and Circuits

---

![image_1](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_3.png)

![image_4](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_4.png)

![image_5](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_5.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_10.png)

![image_11](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_11.png)

![image_12](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_12.png)

![image_13](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_13.png)

![image_14](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_14.png)

![image_15](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_15.png)

![image_16](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_16.png)

![image_17](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_17.png)

![image_18](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_18.png)

![image_19](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_19.png)

![image_20](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_20.png)

![image_21](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_21.png)

![image_22](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_22.png)

![image_23](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_23.png)

![image_24](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_24.png)

![image_25](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_25.png)

![image_26](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_26.png)

![image_27](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_27.png)

![image_28](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_28.png)

![image_29](8%20-%20Currents%20and%20Circuits/8-01%20-%20Currents%20and%20Circuits/image_29.png)

---

1. If 20 C of charge passes a point in 5 s, what is the magnitude of the electric current?

```js
let q = 20; // C
let t = 5; // s
let I = q / t; // A
console.log('I =', I, 'A');
// I = 4 A
```

---

2. A light bulb in a lamp uses 0.55 A of current when a voltage of 110 V is applied to it. How much power does the electric light bulb use?

```js
let I = 0.55; // A
let DV = 110; // V
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 60.50000000000001 W
console.log('P =', Number(P.toPrecision(1)), 'W');
// P = 60 W
```

---

3. An electric oven has a power supply of 220 V and a power rating of 7.3 kW. How much electric current does it draw?

```js
let DV = 220; // V
let P = 7300; // W
let I = P / DV; // A
console.log('I =', I, 'A');
// I = 33.18181818181818 A
console.log('I =', I.toPrecision(2), 'A');
// I = 33 A
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 71

---

### 8.02: Current Electric Forces

---

![image_1](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_3.png)

![image_4](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_4.png)

![image_5](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_5.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_10.png)

![image_11](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_11.png)

![image_12](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_12.png)

![image_13](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_13.png)

![image_14](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_14.png)

![image_15](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_15.png)

![image_16](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_16.png)

![image_17](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_17.png)

![image_18](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_18.png)

![image_19](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_19.png)

![image_20](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_20.png)

![image_21](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_21.png)

![image_22](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_22.png)

![image_23](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_23.png)

![image_24](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_24.png)

![image_25](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_25.png)

![image_26](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_26.png)

![image_27](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_27.png)

![image_28](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_28.png)

![image_29](8%20-%20Currents%20and%20Circuits/8-02%20-%20Current%20Electric%20Forces/image_29.png)

---

1. A 30.0 V battery maintains a current of 3.0 A through a resistor. What is value of the electric resistance?

```js
let DV = 30.0; // V
let I = 3.0; // A
let R = DV / I; // ohmms
console.log('R =', R, 'ohm');
// R = 10 ohm
console.log('R =', R.toFixed(1), 'ohm');
// R = 10.0 ohm
```

---

2. If a heater has a resistance of 5.0 Ω and draws 12.0 A, then what power does it consume?

```js
let I = 12.0; // A
let R = 5.0; // ohm
let P = Math.pow(I, 2) * R; // W
console.log('P =', P, 'W');
// P = 720 W
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 72

---

### 8.03: Series Circuits

---

![image_1](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_3.png)

![image_4](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_4.png)

![image_5](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_5.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_10.png)

![image_11](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_11.png)

![image_12](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_12.png)

![image_13](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_13.png)

![image_14](8%20-%20Currents%20and%20Circuits/8-03%20-%20Series%20Circuits/image_14.png)

---

1. A 12.0 volt battery maintains a current through a light bulb that has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R = 2.0; // ohm
let I = DV / R; // A
console.log('I =', I, 'A');
// I = 6 A
console.log('I =', I.toFixed(1), 'A');
// I = 6.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 72 W
```

---

2. A 12.0 volt battery maintains a current through two light bulbs, each of which has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R1 = 2.0; // ohm
let R2 = 2.0; // ohm
let Req = R1 + R2; // ohm
console.log('Req =', Req, 'ohm');
// Req = 4 ohm
let I = DV / Req; // A
console.log('I =', I, 'A');
// I = 3 A
console.log('I =', I.toFixed(1), 'A');
// I = 3.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 36 W
```

---

3. A 12.0 volt battery maintains a current through three light bulbs, each of which has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R1 = 2.0; // ohm
let R2 = 2.0; // ohm
let R3 = 2.0; // ohm
let Req = R1 + R2 + R3; // ohm
console.log('Req =', Req, 'ohm');
// Req = 6 ohm
let I = DV / Req; // A
console.log('I =', I, 'A');
// I = 2 A
console.log('I =', I.toFixed(1), 'A');
// I = 2.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 24 W
```

---

4. A 12.0 V battery is hooked up to three resistors in series. The first resistor is 2.0 Ω, the second is 3.0 Ω, and the third is 5.0 Ω. What is the current in the circuit? What is the total power? How much voltage drops across each resistor?

```js
let DVtotal = 12.0; // V
let R1 = 2.0; // ohm
let R2 = 3.0; // ohm
let R3 = 5.0; // ohm
let Req = R1 + R2 + R3; // ohm
console.log('Req =', Req, 'ohm');
// Req = 10 ohm
let Itotal = DVtotal / Req; // A
console.log('Itotal =', Itotal, 'A');
// Itotal = 1.2 A
console.log('Itotal =', Itotal.toFixed(2), 'A');
// Itotal = 1.20 A
let P = Itotal * DVtotal; // W
console.log('P =', P, 'W');
// P = 14.399999999999999 W
console.log('P =', P.toPrecision(3), 'W');
// P = 14.4 W
let DV1 = Itotal * R1; // V
console.log('DV1 =', DV1, 'V');
// DV1 = 2.4 V
let DV2 = Itotal * R2; // V
console.log('DV2 =', DV2, 'V');
// DV2 = 3.5999999999999996 V
console.log('DV2 =', DV2.toFixed(1), 'V');
// DV2 = 3.6 V
let DV3 = Itotal * R3; // V
console.log('DV3 =', DV3, 'V');
// DV3 = 6 V
console.log('DV3 =', DV3.toFixed(1), 'V');
// DV3 = 6.0 V
DVtotal123 = DV1 + DV2 + DV3;
console.log('DVtotal123 =', DVtotal123, 'V');
// DVtotal123 = 12 V
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 73

---

### 8.04: Parallel Circuits

---

![image_1](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_3.png)

![image_4](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_4.png)

![image_5](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_5.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_10.png)

![image_11](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_11.png)

![image_12](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_12.png)

![image_13](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_13.png)

![image_14](8%20-%20Currents%20and%20Circuits/8-04%20-%20Parallel%20Circuits/image_14.png)

---

1. A 12.0 volt battery maintains a current through a light bulb that has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R = 2.0; // ohm
let I = DV / R; // A
console.log('I =', I, 'A');
// I = 6 A
console.log('I =', I.toFixed(1), 'A');
// I = 6.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 72 W
```

---

2. A 12.0 volt battery maintains a current through two light bulbs arranged in parallel, each of which has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R = 2.0; // ohm
let Req = 1 / (1 / R + 1 / R); // ohm
console.log('Req =', Req, 'ohm');
let I = DV / Req; // A
console.log('I =', I, 'A');
// I = 12 A
console.log('I =', I.toFixed(1), 'A');
// I = 12.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 144 W
```

---

3. A 12.0 volt battery maintains a current through three light bulbs arranged in parallel, each of which has a resistance of 2.0 Ω. What is the current and power in the circuit?

```js
let DV = 12.0; // V
let R = 2.0; // ohm
let Req = 1 / (1 / R + 1 / R + 1 / R); // ohm
console.log('Req =', Req, 'ohm');
// Req = 0.6666666666666666 ohm
console.log('Req =', Req.toFixed(2), 'ohm');
// Req = 0.67 ohm
let I = DV / Req; // A
console.log('I =', I, 'A');
// I = 18 A
console.log('I =', I.toFixed(1), 'A');
// I = 18.0 A
let P = I * DV; // W
console.log('P =', P, 'W');
// P = 216 W
```

---

4. A 12.0 V battery is hooked up to three resistors in parallel. The first resistor is 2.0 Ω, the second is 3.0 Ω, and the third is 5.0 Ω. What is the current in the circuit? What is the total power? How much current goes through each resistor?

```js
let DVtotal = 12.0; // V
let R1 = 2.0; // ohm
let R2 = 3.0; // ohm
let R3 = 5.0; // ohm
let Req = 1 / (1 / R1 + 1 / R2 + 1 / R3); // ohm
console.log('Req =', Req, 'ohm');
// Req = 10 ohm
console.log('Req =', Req.toFixed(2), 'ohm');
// Req = 0.97 ohm
let Itotal = DVtotal / Req; // A
console.log('Itotal =', Itotal, 'A');
// Itotal = 12.399999999999999 A
console.log('Itotal =', Itotal.toPrecision(2), 'A');
// Itotal = 12 A
Itotal = Number(Itotal.toPrecision(2));
let Ptotal = Itotal * DVtotal; // W
console.log('Ptotal =', Ptotal, 'W');
// Ptotal = 144 W
let l1 = DVtotal / R1; // A
console.log('l1 =', l1, 'A');
// l1 = 6 A
console.log('l1 =', l1.toFixed(1), 'A');
// l1 = 6.0 A
let l2 = DVtotal / R2; // A
console.log('l2 =', l2, 'A');
// l2 = 4 A
console.log('l2 =', l2.toFixed(1), 'A');
// l2 = 4.0 A
let l3 = DVtotal / R3; // A
console.log('l3 =', l3, 'A');
// l3 = 2.4 A
let ltotal = l1 + l2 + l3; // A
console.log('ltotal =', ltotal, 'A');
// ltotal = 12.4 A
console.log('ltotal =', Number(ltotal.toPrecision(2)), 'A');
// ltotal = 12 A
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 74

---

### 8.05: Combined Circuits

---

![image_1](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_1.png)

![image_2](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_2.png)

![image_3](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_3.png)

![image_6](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_6.png)

![image_7](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_7.png)

![image_8](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_8.png)

![image_9](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_9.png)

![image_10](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_10.png)

---

1. What is the equivalent resistance of a combined circuit with the arrangement of resistors shown? Calculate the total current moving through the circuit.

![image_4](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_4.png)

```js
let R1 = 10.0; // ohm
let R2 = 13.0; // ohm
let R3 = 15.0; // ohm
let R4 = 35.0; // ohm
let DVtotal = 60.0; // V
let R_2_3 = 1 / (1 / R2 + 1 / R3); // ohm
console.log('R_2_3 =', R_2_3, 'ohm');
// R_2_3 = 6.964285714285714 ohm
console.log('R_2_3 =', R_2_3.toFixed(1), 'ohm');
// R_2_3 = 7.0 ohm
let Req = R1 + R_2_3 + R4; // ohm
console.log('Req =', Req, 'ohm');
// Req = 51.964285714285715 ohm
console.log('Req =', Req.toFixed(1), 'ohm');
// Req = 52.0 ohm
let ltotal = DVtotal / Req; // A
console.log('ltotal =', ltotal, 'A')
// ltotal = 1.1546391752577319 A
console.log('ltotal =', ltotal.toFixed(2), 'A');
// ltotal = 1.15 A
```

---

2. What is the equivalent resistance of a combined circuit with the arrangement of resistors shown? Calculate the total current moving through the circuit.

![image_5](8%20-%20Currents%20and%20Circuits/8-05%20-%20Combined%20Circuits/image_5.png)

```js
let R1 = 10.0; // ohm
let R_2_3 = 7.0; // ohm
let R4 = 35.0; // ohm
let ltotal = 1.15; // A
let DV1 = ltotal * R1; // V
console.log('DV1 =', DV1, 'V');
// DV1 = 11.5 V
console.log('DV1 =', DV1.toPrecision(3), 'V');
// DV1 = 11.5 V
let DV_2_3 = ltotal * R_2_3; // V
console.log('DV_2_3 =', DV_2_3, 'V');
// DV_2_3 = 8.049999999999999 V
console.log('DV_2_3 =', DV_2_3.toPrecision(3), 'V');
// DV_2_3 = 8.05 V
let DV4 = ltotal * R4; // V
console.log('DV4 =', DV4, 'V');
// DV4 = 40.25 V
console.log('DV4 =', DV4.toPrecision(3), 'V');
// DV4 = 40.3 V
DVtotal = DV1 + DV_2_3 + DV4; // V
console.log('DVtotal =', DVtotal, 'V');
// DVtotal = 59.8 V
console.log('DVtotal =', DVtotal.toPrecision(2), 'V');
// DVtotal = 60 V
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 75

---

## 9: Magnetism

---

### 9.01: Magnets and Magnetic Fields

---

![image_1](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_1.png)

![image_2](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_2.png)

![image_3](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_3.png)

![image_4](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_4.png)

![image_5](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_5.png)

![image_6](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_6.png)

![image_7](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_7.png)

![image_8](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_8.png)

![image_9](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_9.png)

![image_10](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_10.png)

![image_11](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_11.png)

![image_12](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_12.png)

![image_13](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_13.png)

![image_14](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_14.png)

![image_15](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_15.png)

![image_16](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_16.png)

![image_17](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_17.png)

![image_18](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_18.png)

![image_19](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_19.png)

![image_20](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_20.png)

![image_21](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_21.png)

![image_22](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_22.png)

![image_23](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_23.png)

![image_24](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_24.png)

![image_25](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_25.png)

![image_26](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_26.png)

![image_27](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_27.png)

![image_28](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_28.png)

![image_29](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_29.png)

![image_30](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_30.png)

![image_31](9%20-%20Magnetism/9-01%20-%20Magnets%20and%20Magnetic%20Fields/image_31.png)

---

1. A magnetic field of magnitude B = 0.10 T is directed perpendicular to a circular loop of wire of radius 0.22 m. Find the magnetic flux through the wire.

```js
let r = 0.22; // m
let B = 0.10; // T
let A = Math.PI * Math.pow(r, 2); // m^2
console.log('A =', A, 'm^2');
// A = 0.152053084433746 m^2
console.log('A =', A.toFixed(3), 'm^2');
// A = 0.152 m^2
let phi = B * A; // T * m^2
console.log('phi =', phi, 'T * m^2');
// phi = 0.0152053084433746 T * m^2
console.log('phi =', phi.toFixed(3), 'T * m^2');
// phi = 0.015 T * m^2
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 76

---

### 9.02: Forces in Magnetic Fields

---

![image_1](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_1.png)

![image_2](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_2.png)

![image_3](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_3.png)

![image_4](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_4.png)

![image_5](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_5.png)

![image_6](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_6.png)

![image_7](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_7.png)

![image_8](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_8.png)

![image_9](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_9.png)

![image_10](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_10.png)

![image_11](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_11.png)

![image_12](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_12.png)

![image_13](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_13.png)

![image_14](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_14.png)

![image_15](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_15.png)

![image_16](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_16.png)

![image_17](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_17.png)

![image_18](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_18.png)

![image_19](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_19.png)

![image_20](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_20.png)

![image_21](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_21.png)

![image_22](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_22.png)

![image_23](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_23.png)

![image_24](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_24.png)

![image_25](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_25.png)

![image_26](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_26.png)

![image_27](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_27.png)

![image_28](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_28.png)

![image_29](9%20-%20Magnetism/9-02%20-%20Forces%20in%20Magnetic%20Fields/image_29.png)

---

1. A 6.0 m section of wire carries a current of 4.0 A from north to south. It is in a uniform magnetic field of 0.30 T pointing upward. What is the magnitude and direction of the magnetic force on the wire?

* You know the current I, the length L of the section of wire, and the magnetic field B, which enables you to calculate the magnitude of the magnetic force. You also know the direction of the current and the magnetic field and can use the right-hand rule to find the direction of the force.

```js
let I = 4.0; // A
let L = 6.0; // m
let B = 0.30; // T
FB = I * L * B; // N
console.log('FB =', FB, 'N');
// FB = 7.199999999999999 N
console.log('FB =', FB.toPrecision(2), 'N');
// FB = 7.2 N
```

* Find the direction of the force. Picture your right hand's fingers pointing in the direction of the magnetic field B upward and your thumb toward the current I to the south. The palm of your hand would then point west, so the force is toward the west.

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 77

---

### 9.03: Electromagnetic Induction

---

![image_1](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_1.png)

![image_2](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_2.png)

![image_3](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_3.png)

![image_4](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_4.png)

![image_5](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_5.png)

![image_6](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_6.png)

![image_7](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_7.png)

![image_8](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_8.png)

![image_9](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_9.png)

![image_10](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_10.png)

![image_11](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_11.png)

![image_12](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_12.png)

![image_13](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_13.png)

![image_14](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_14.png)

![image_15](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_15.png)

![image_19](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_19.png)

![image_20](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_20.png)

![image_23](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_23.png)

![image_24](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_24.png)

![image_25](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_25.png)

![image_26](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_26.png)

![image_27](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_27.png)

![image_28](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_28.png)

![image_29](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_29.png)

![image_30](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_30.png)

---

1. A circular loop of wire is cut at one point to connect it to the leads of a galvanometer. The loop has a radius of 1.2 cm. If a magnetic field perpendicular to the area of the coil changes from 0.50 T to 0.10 T in 0.10 s, what is the emf across the galvanometer during that time?

* You know the area of the loop perpendicular to the field, the initial and final magnetic field B, and the time of the change. Therefore you can find the change in flux divided by the time of the change.

```js
let theta = 0; // radians
let cosTheta = Math.cos(theta); // 1
let r = 0.012; // m
let A = Math.PI * Math.pow(r, 2); // m^2
let B1 = 0.50; // T
let B2 = 0.10; // T
let DB = B1 - B2; // T
let DphiB = A * cosTheta * DB; // T * m^2
console.log('DphiB =', DphiB.toExponential(), 'T*m^2');
// DphiB = 1.8095573684677208e-4 T*m^2
console.log('DphiB =', Number(DphiB.toPrecision(3)).toExponential(), 'T*m^2');
// DphiB = 1.81e-4 T*m^2
let DT = 0.10; // s
let e = -DphiB / DT; // V
console.log('e =', e.toExponential(), 'V');
// e = -1.8095573684677208e-3 V
console.log('e =', Number(e.toPrecision(2)).toExponential(), 'V');
// e = -1.8e-3 V
```

* The induced emf would have been much larger with more turns of wire.

---

2. A circular loop of wire is connected to the leads of a galvanometer. The loop has a radius of 1.2 cm. The uniform magnetic field is perpendicular to the area of the coil, and it changes from 0.50 T to 0.10 T in 0.10 s. The emf across the galvanometer during that time is ε = 1.8 × 10^-3 V. Find the direction of the induced emf, where the magnetic field B is downward and decreasing.

* The magnetic field points downward. The field is decreasing to produce a decreasing flux. According to Lenz's law, the current from the emf produced by this change must oppose the decrease in flux.

![image_16](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_16.jpg)

* To oppose the decrease in flux inducing the emf, the emf must be in a direction to produce an upward magnetic field. Apply the right-hand rule to find which current direction has this effect.

![image_17](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_17.jpg)

* The direction of the induced current and induced emf must be as shown.

---

3. A magnet is moved into a coil connected to a galvanometer as shown. Find the direction of the induced emf in the coil.

![image_18](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_18.jpg)

* You know that the magnetic field points from the north pole of the magnet so that the magnetic flux through the coil, as drawn, is increasing. You know Lenz’s law, that the emf which results is in the direction that would induce a current to oppose the original change in flux.

* Since the magnetic flux is increasing and moving downward, the emf that would oppose the change in magnetic flux would create an upward magnetic field.

* Use the right-hand rule to see that a current in the direction marked on the diagram would cause an upward magnetic field.

---

4. A straight wire of length 1.2 m moves through a magnetic field at velocity v = 1.0 m/s, cutting directly across magnetic field lines. Find the emf that results.

![image_21](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_21.jpg)

* What is known?

![image_22](9%20-%20Magnetism/9-03%20-%20Electromagnetic%20Induction/image_22.png)

* Calculate the emf.

```js
let B = 0.10; // T
let L = 1.2; // m
let v = 1.0; // m/s
let e = B * L * v; // V
console.log('e =', e, 'V');
// e = 0.12 V
```

---

5. A transformer has 2,000 windings in its primary coil and uses 120 V AC input. How many windings should it have in its secondary coil to produce an output voltage of 1.5 V?

* The number of turns of wire in the primary coil and the input and output voltages are known. The ratio of the primary and secondary turns of wire is equal to the ratio of the primary and secondary voltages.

```js
let Vs = 1.5; // V
let Np = 2000; // windings
let Vp = 110; // V
let Ns = Vs * Np / Vp; // turns
console.log('Ns =', Ns, 'turns');
// Ns = 27.272727272727273 turns
console.log('Ns =', Math.round(Ns), 'turns');
// Ns = 27 turns
```

* The number of secondary windings needed is much smaller than the number of primary windings, as expected.

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 78

---

## 10: Modern Physics

---

### 10.01: Atomic Spectra and Quantum Theory

---

![image_1](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_1.png)

![image_2](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_2.png)

![image_3](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_3.png)

![image_4](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_4.png)

![image_5](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_5.png)

![image_6](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_6.png)

![image_7](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_7.png)

![image_8](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_8.png)

![image_9](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_9.png)

![image_10](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_10.png)

![image_11](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_11.png)

![image_12](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_12.png)

![image_13](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_13.png)

![image_14](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_14.png)

![image_15](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_15.png)

![image_16](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_16.png)

![image_17](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_17.png)

![image_18](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_18.png)

![image_19](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_19.png)

![image_20](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_20.png)

![image_21](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_21.png)

![image_22](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_22.png)

![image_23](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_23.png)

![image_24](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_24.png)

![image_25](10%20-%20Modern%20Physics/10-01%20-%20Atomic%20Spectra%20and%20Quantum%20Theory/image_25.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 79

---

### 10.02: The Nature of Light and the Photoelectric Effect

---

![image_1](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_1.png)


![image_2](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_2.png)


![image_3](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_3.png)


![image_4](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_4.png)


![image_5](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_5.png)


![image_6](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_6.png)


![image_7](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_7.png)


![image_8](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_8.png)


![image_9](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_9.png)


![image_10](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_10.png)


![image_11](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_11.png)


![image_12](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_12.png)


![image_13](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_13.png)


![image_14](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_14.png)


![image_15](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_15.png)


![image_16](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_16.png)


![image_17](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_17.png)


![image_18](/10%20-%20Modern%20Physics/10-02%20-%20The%20Nature%20of%20Light%20and%20the%20Photoelectric%20Effect/image_18.png)

---

1. What is the energy of a photon of green light (λ=532 nm) in joules? Remember, Planck's constant h = 6.63 × 10^-34 J * s.

```js
const h = 6.63 * Math.pow(10, -34); // J * s
const c = 3.00 * Math.pow(10, 8); // m/s
let wavelength = 5.32 * Math.pow(10, -7); // m
let f = c / wavelength; // Hz
console.log('f =', f.toExponential(), 'Hz');
// f = 5.639097744360901e+14 Hz
console.log('f =', Number(f.toPrecision(3)).toExponential(), 'Hz');
// f = 5.64e+14 Hz
let E = h * f; // J
console.log('E =', E.toExponential(), 'J');
// E = 3.738721804511277e-19 J
console.log('E =', Number(E.toPrecision(3)).toExponential(), 'J');
// E = 3.74e-19 J
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 80

---

### 10.03: Relativity

---

![image_1](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_1.png)

![image_2](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_2.png)

![image_3](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_3.png)

![image_4](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_4.png)

![image_5](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_5.png)

![image_6](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_6.png)

![image_7](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_7.png)

![image_8](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_8.png)

![image_9](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_9.png)

![image_10](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_10.png)

![image_11](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_11.png)

![image_12](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_12.png)

![image_13](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_13.png)

![image_14](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_14.png)

![image_15](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_15.png)

![image_16](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_16.png)

![image_17](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_17.png)

![image_18](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_18.png)

![image_19](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_19.png)

![image_20](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_20.png)

![image_21](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_21.png)

![image_22](10%20-%20Modern%20Physics/10-03%20-%20Relativity/image_22.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 81

---

### 10.04: Structure of the Nucleus

---

![image_1](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_1.png)

![image_2](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_2.png)

![image_3](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_3.png)

![image_4](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_4.png)

![image_5](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_5.png)

![image_6](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_6.png)

![image_7](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_7.png)

![image_8](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_8.png)

![image_9](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_9.png)

![image_10](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_10.png)

![image_11](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_11.png)

![image_12](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_12.png)

![image_13](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_13.png)

![image_14](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_14.png)

![image_15](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_15.png)

![image_16](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_16.png)

![image_17](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_17.png)

![image_18](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_18.png)

![image_19](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_19.png)

![image_20](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_20.png)

![image_21](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_21.png)

![image_22](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_22.png)

![image_23](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_23.png)

![image_24](10%20-%20Modern%20Physics/10-04%20-%20Structure%20of%20the%20Nucleus/image_24.png)

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 82

---

### 10.05: Radioactivity

---

![image_1](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_1.png)

![image_2](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_2.png)

![image_3](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_3.png)

![image_4](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_4.png)

![image_5](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_5.png)

![image_6](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_6.png)

![image_7](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_7.png)

![image_8](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_8.png)

![image_9](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_9.png)

![image_10](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_10.png)

![image_11](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_11.png)

![image_12](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_12.png)

![image_13](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_13.png)

![image_14](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_14.png)

![image_15](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_15.png)

![image_16](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_16.png)

![image_17](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_17.png)

![image_18](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_18.png)

![image_19](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_19.png)

![image_20](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_20.png)

![image_21](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_21.png)

![image_22](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_22.png)

![image_23](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_23.png)

![image_24](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_24.png)

![image_25](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_25.png)

![image_26](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_26.png)

![image_27](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_27.png)

![image_28](10%20-%20Modern%20Physics/10-05%20-%20Radioactivity/image_28.png)

---

1. Carbon-14 or C14 has a half life 5,730 years. If you start with 8.00 × 10^-6 g of C14, how much will you have after 17,190 years?

```js
let iT = 5730; // years
let fT = 17190; // years
let iM = 8.00 * Math.pow(10, -6); // g
let number_of_halflives = fT / iT;
console.log('number_of_halflives =', number_of_halflives);
// number_of_halflives = 3
let fraction_remaining = Math.pow(0.5, number_of_halflives);
console.log('fraction_remaining =', fraction_remaining);
// fraction_remaining = 0.125
let fM = fraction_remaining * iM; // g
console.log('fM =', fM.toExponential(), 'g');
// fM = 1e-6 g
console.log('fM =', fM.toExponential(2), 'g');
// fM = 1.00e-6 g
```

---

#### Problem Set

* "Physics: Problems and Solutions" - Problem Set 83

---
