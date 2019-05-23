import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
  <h1>XboxOne Games</h1>
  <router-outlet></router-outlet>
  `,
  styles: []
})
export class AppComponent {
  title = 'xbox-one-backcompat-games';
}
