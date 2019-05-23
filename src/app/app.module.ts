import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GamesListComponent } from './games-list/games-list.component';
import { SearchComponent } from './search/search.component';
import { GameComponent } from './game/game.component';
import { HttpClientModule } from '@angular/common/http';
import { GamesSearchPipe } from './games-search.pipe';
import { HaveGamePipe } from './have-game.pipe';
import { FormsModule, ReactiveFormsModule } from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    GamesListComponent,
    SearchComponent,
    GameComponent,
    GamesSearchPipe,
    HaveGamePipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
