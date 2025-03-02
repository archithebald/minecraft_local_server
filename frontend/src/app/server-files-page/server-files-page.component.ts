import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ServerPageLeftComponent } from '../server-page-left/server-page-left.component';

@Component({
  selector: 'app-server-files-page',
  standalone: true,
  imports: [RouterOutlet, ServerPageLeftComponent],
  templateUrl: './server-files-page.component.html',
  styleUrl: './server-files-page.component.css'
})
export class ServerFilesPageComponent {

}
