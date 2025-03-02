import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ServerPageLeftComponent } from '../server-page-left/server-page-left.component';

@Component({
  selector: 'app-server-console-page',
  standalone: true,
  imports: [RouterOutlet, ServerPageLeftComponent],
  templateUrl: './server-console-page.component.html',
  styleUrl: './server-console-page.component.css',
})
export class ServerConsolePageComponent {}
