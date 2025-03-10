import { Component } from '@angular/core';
import { ServerPageLeftComponent } from '../server-page-left/server-page-left.component';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-file-page',
  imports: [ServerPageLeftComponent, RouterOutlet],
  templateUrl: './file-page.component.html',
  styleUrl: './file-page.component.css'
})
export class FilePageComponent {

}
