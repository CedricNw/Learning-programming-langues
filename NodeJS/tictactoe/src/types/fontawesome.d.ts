declare module '@fortawesome/fontawesome-svg-core' {
  export const library: any;
  export function dom(): any;
  export function config(): any;
}

declare module '@fortawesome/vue-fontawesome' {
  import { Component } from 'vue';
  export const FontAwesomeIcon: Component;
}

declare module '@fortawesome/free-solid-svg-icons' {
  const content: any;
  export const faHome: any;
  export const faUser: any;
  export const faBars: any;
  export const faAngleDoubleLeft: any;
}