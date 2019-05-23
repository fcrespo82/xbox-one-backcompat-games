import { Pipe, PipeTransform } from '@angular/core';
import { GameComponent } from './game/game.component';

@Pipe({
  name: 'haveGame'
})
export class HaveGamePipe implements PipeTransform {

  transform(games: GameComponent[], have: any): GameComponent[] {
    return games.filter(game => {
      if (have === true) {
        if (game.have === true) {
          return true
        } else {
          return false
        }
      } else {
        return true
      }
    })
  }

}
