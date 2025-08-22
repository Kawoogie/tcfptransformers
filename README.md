<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!-- -->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Kawoogie/tcfptransformers">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">TCFP Data Handling Package.</h3>

  <p align="center">
    This Python package contains custom tranformers for Scikit-Learn pipelines to work with the TCFP protocol.
    <br />
    <a href="https://github.com/Kawoogie/tcfptransformers"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Kawoogie/tcfptransformers">View Demo</a>
    ·
    <a href="https://github.com/Kawoogie/tcfptransformers/issues">Report Bug</a>
    ·
    <a href="https://github.com/Kawoogie/tcfptransformers/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This Python package contains custom tranformers for Scikit-Learn pipelines to work with the TCFP protocol. The transformers are meant to modify and prepare the data of the TCFP protocol for input into a machine learning model. The transformers have been written so that they can be incorportated into a pipeline.
<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started

This is a custom package. Start by installing the package, then follow the example to understand how to use the major functions.

Start by creating an environment to install the package
```
conda create -n "myenv" python=3.10.17 ipython
```

Activate the environment
```
conda activate myenv
```

Install the required packages
```
pip install pandas
pip install matplotlib
pip install -U scikit-learn
```


### Prerequisites
This code was tested on Python 3.9

This code requires the following packages:
- Numpy 1.19.2 or higher
- Scipy 1.5.2 or higher
- Scikit Learn 1.2.1 or higher
  

### Installation
This code can be imported by using: 
```
pip install git+https://github.com/Kawoogie/tcfptransformers.git
```

Note: Make sure git is updated before install
For Windows:
```
git update-git-for-windows
```
For Mac:
```
git update
```
Also, ensure that long filepath names are enabled on git:
```
git config --global core.longpaths true
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

  


<!-- USAGE EXAMPLES -->
## Usage
Here's an example of how to use this package to transform the data: 
### Example 
```


```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Kawoogie/tcfptransformers/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
Project Link: [https://github.com/Kawoogie/tcfpdatahandling](https://github.com/Kawoogie/tcfptransformers)

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Kawoogie/tcfptransformers.svg?style=for-the-badge
[contributors-url]: https://github.com/Kawoogie/tcfptransformers/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Kawoogie/tcfptransformers.svg?style=for-the-badge
[forks-url]: https://github.com/Kawoogie/tcfptransformers/network/members
[stars-shield]: https://img.shields.io/github/stars/Kawoogie/tcfptransformers.svg?style=for-the-badge
[stars-url]: https://github.com/Kawoogie/tcfptransformers/stargazers
[issues-shield]: https://img.shields.io/github/issues/Kawoogie/tcfptransformers.svg?style=for-the-badge
[issues-url]: https://github.com/Kawoogie/tcfptransformers/issues
[license-shield]: https://img.shields.io/github/license/Kawoogie/tcfptransformers.svg?style=for-the-badge
[license-url]: https://github.com/Kawoogie/tcfptransformers/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/lee-sikstrom-a6472a113
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com



