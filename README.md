<p align=""center>


<h1>
  <br>
  Endian String Convert
  <br>
</h1>

[![Issuse]( https://img.shields.io/github/issues/kunaldesign/Endian)](https://github.com/kunaldesign/Endian/issues)
[![Fork](https://img.shields.io/github/forks/kunaldesign/Endian)](https://github.com/kunaldesign/Endian)
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](/CONTRIBUTING.md)
[![stars](https://img.shields.io/github/stars/kunaldesign/Endian)](https://github.com/kunaldesign/Endian)
[![License](https://img.shields.io/github/license/kunaldesign/Endian)](/LICENSE)
[![Tweet](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fkunaldesign%2FEndian)](https://twitter.com/kunalhedaoo25)
<!-- [![PyPI](https://img.shields.io/pypi/v/Endian?style=plastic)]() -->


[![Check it out](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)
[![license](https://forthebadge.com/images/badges/open-source.svg)](/LICENSE)
[![developer](https://forthebadge.com/images/badges/built-by-developers.svg)](/CONTRIBUTING.md)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
<!-- [![html](https://forthebadge.com/images/badges/validated-html5.svg)](/index.html) -->






</p>

<p align="center">
  <a href="#introduction-">Introduction</a> •
  <a href="#usage-">Usage</a> •
  <a href="#browser-support-">Browser Support</a> •
  <a href="#credits-">Credits</a> •
  <a href="#contributing-️">Contributors</a> •
  <a href="#license-">License</a>
</p>


---------------------------------------------------------------------------

# Table of Contents 🚩

- [Table of Contents 🚩](#table-of-contents-)
- [Introduction 🪶](#introduction-)
- [Prerequisites 📐](#prerequisites-)
- [System Support 🌏](#system-support-)
- [Usage 🔄](#usage-)
    - [For installation from testing repo](#for-installation-from-testing-repo)
    - [For installation from main repo](#for-installation-from-main-repo)
    - [For Using Libary](#for-using-libary)
      - [to change string big to little](#to-change-string-big-to-little)
      - [to change string little to big](#to-change-string-little-to-big)
      - [to change decimal to hexadecimal string](#to-change-decimal-to-hexadecimal-string)
      - [to create two's complemate of the hexadecimal string](#to-create-twos-complemate-of-the-hexadecimal-string)
- [Credits 🏅](#credits-)
- [Contributing 🗯️](#contributing-️)
- [Support ⛑️](#support-️)
- [Team 👩‍🏭](#team-)
  - [| Shubham Aglawe                                                                                         | Kunal Hedaoo                                                          |](#-shubham-aglawe------------------------------------------------------------------------------------------kunal-hedaoo----------------------------------------------------------)
- [Donation 💸](#donation-)
- [License 📜](#license-)

---
# Introduction 🪶

<table>
<tr>
<td>
  Hexadecimal operations and the byte operations
</td>
</tr>
</table>

---

# Prerequisites 📐

The things you need before go to website.

- Install python3 in the system.
- Install pip3 package.

---

# System Support 🌏


| <img alt="UbuntuCoF" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/UbuntuCoF.svg/512px-UbuntuCoF.svg.png" alt="Ubuntu" width="16px" height="16px" /> Ubuntu | <img alt="Microsoft logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/256px-Microsoft_logo.svg.png" alt="Window" width="16px" height="16px" /> Window | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/MacOS_logo_%282017%29.svg/512px-MacOS_logo_%282017%29.svg.png" alt="MacOS" width="16px" height="16px" /> MacOS | <img src="https://seeklogo.com/images/C/centos-logo-494F57D973-seeklogo.com.png" alt="centos" width="16px" height="16px" /> Centos | <img src="https://elinux.org/images/c/cb/Raspberry_Pi_Logo.svg" alt="Firefox" width="16px" height="16px" /> RaspberryPi |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                               Yes                                                                                |                                                                                   Yes                                                                                   |                                                                             Yes                                                                              |                                                                               Yes                                                                                |                                                                                Yes                                                                                 |

---

# Usage 🔄

- Installation and uses of the libary.


### For installation from testing repo

- Install python libary using pip3

```python
  pip3 install -i https://test.pypi.org/simple/ Endian
```

OR

```python
  python3 -m pip install -i https://test.pypi.org/simple/ Endian
```

### For installation from main repo

- Install python libary using pip3

```python
  pip3 install -i https://test.pypi.org/simple/ Endian
```

OR

```python
  python3 -m pip install -i https://test.pypi.org/simple/ Endian
```

### For installation from main repo

- Install python libary using pip3

```python
  pip3 install Endian
```

OR

```python
  python3 -m pip install Endian
```

### For Using Libary

#### to change string big to little 

- import libary in the python  
```python
  from Endian.endian import big_to_little_str
```
- calling function
```python
  big_to_little_str("ASFDQW")
```

#### to change string little to big 

- import libary in the python  
```python
  from Endian.endian import little_to_big_str
```
- calling function
```python
  little_to_big_str("QWFDAS")
```

#### to change decimal to hexadecimal string

- import libary in the python  
```python
  from Endian.endian import endian_hex_str
```
- calling function
```python
  endian_hex_str(1234)
```

#### to change string little to big 

- import libary in the python  
```python
  from Endian.endian import little_to_big_str
```
- calling function
```python
  little_to_big_str("QWFDAS")
```
#### to change decimal to hexadecimal string

- import libary in the python  
```python
  from Endian.endian import endian_hex_str
```
- calling function
```python
  endian_hex_str(1234)
```

#### to create two's complemate of the hexadecimal string

- import libary in the python  
```python
  from Endian.endian import twos_com_str
```
- calling function
```python
  twos_com_str("QWFDAS")
```

# Credits 🏅

- [@kunaldesign](https://github.com/kunaldesign) 🥇
- [@s-rebel](https://github.com/s-rebel) 🥈

---

# Contributing 🗯️

- [Code of Conduct](/CODE_OF_CONDUCT.md)
- [Contributing Guideline](/CONTRIBUTING.md)
- [Commit Convention](/.github/ISSUE_TEMPLATE/COMMIT_MESSAGE_CONVENTION.md)
- [Issue Guidelines](/.github/ISSUE_TEMPLATE)


---
# Support ⛑️
 
 - @kunaldesign - kunalhedaoo25@gmail.com 
 - @s-rebel - aglaweshubham17@gmail.com


 
---
# Team 👩‍🏭

 [![Shubham Aglawe](https://avatars.githubusercontent.com/u/95236180?v=4)](https://github.com/s-rebel) | [![Kunal Hedaoo](https://avatars.githubusercontent.com/u/49153579?v=4)](https://github.com/kunaldesign) |
------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| [Shubham Aglawe](https://github.com/s-rebel)                                                                                         | [Kunal Hedaoo](https://github.com/kunaldesign)                                                          |

---
# Donation 💸

<img alt="Donation" src="static/images/Endian%20Donation.png" width="320px" height="320px" />


---

# License 📜

This software is licensed under the [MIT](https://github.com/nhn/tui.editor/blob/master/LICENSE) © [Kunal Hedaoo](https://github.com/nhn).

---