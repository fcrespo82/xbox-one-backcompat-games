import { Pipe, PipeTransform } from '@angular/core';
import { GameComponent } from './game/game.component';

@Pipe({
  name: 'gamesSearch'
})
export class GamesSearchPipe implements PipeTransform {
  transform(games: GameComponent[], filtro: any): GameComponent[] {
    return games.filter(game => {
      if (filtro != null && filtro.trim() != '') {
        return game.title.toLowerCase().includes(filtro.toLowerCase())
      } else {
        return true
      }
    })
  }
}
