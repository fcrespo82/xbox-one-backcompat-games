import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Game } from '../game';

@Component({
  selector: 'games-list',
  templateUrl: './games-list.component.html'
})
export class GamesListComponent implements OnInit {

  allGames: Game[] = []

  constructor(private http: HttpClient, private cdr: ChangeDetectorRef) { }

  ngOnInit() {
    this.getAllGames().subscribe(
      (allGames: Game[]) => {
        this.getMyGames().subscribe(
          (myGames: string[]) => {
            const games = allGames.map((game) => {
              myGames.forEach((regex) => {
                var caseInsensitiveRegex = new RegExp(regex, "i");
                if (caseInsensitiveRegex.test(game.title)) {
                  game.have = true
                }
              })
              return game
            })
            this.allGames = games
            this.cdr.detectChanges()
          })
      })
  }

  getAllGames() {
    return this.http.get("./assets/games.json")
  }

  getMyGames() {
    return this.http.get("./assets/my_games.json")
  }
}
