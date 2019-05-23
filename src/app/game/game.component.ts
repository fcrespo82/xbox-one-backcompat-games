import { Component, OnInit, Input, Injectable } from '@angular/core';

@Component({
  selector: 'game',
  templateUrl: './game.component.html'
})
export class GameComponent implements OnInit {

  @Input() title: string
  @Input() image: string = './assets/images/xbox.gif'
  @Input() have: boolean = false

  constructor() { }

  ngOnInit() {
  }

}
