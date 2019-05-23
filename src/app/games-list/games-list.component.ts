import { Component, OnInit, Output } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DomSanitizer } from '@angular/platform-browser';
import { GameComponent } from '../game/game.component';

@Component({
  selector: 'games-list',
  templateUrl: './games-list.component.html'
})
export class GamesListComponent implements OnInit {

  allGames: any[]

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.listAllGames()
  }

  listAllGames() {
    this.http.get("./assets/games.json").subscribe(
      (data: any[]) => {
        this.allGames = data
        this.listMyGames()
      })
  }

  listMyGames() {
    this.http.get("./assets/my_games.json").subscribe(
      (data: string[]) => {
        this.allGames = this.allGames.map((game, i, a) => {
          data.forEach((regex, i, a) => {
            var caseInsensitiveRegex = new RegExp(regex, "i");
            if (caseInsensitiveRegex.test(game.title)) {
              game.have = true
            }
          })
          return game
        })
      })
  }
}
