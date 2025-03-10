import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterOutlet } from '@angular/router';
import { ServerPageLeftComponent } from '../server-page-left/server-page-left.component';
import { MatIcon, MatIconModule } from '@angular/material/icon';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { ConfigService } from '../config.service';
import { CommonModule, NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-server-files-page',
  standalone: true,
  imports: [NgFor, CommonModule, FormsModule, RouterOutlet, ServerPageLeftComponent, HttpClientModule, MatIcon],
  templateUrl: './server-files-page.component.html',
  styleUrl: './server-files-page.component.css'
})
export class ServerFilesPageComponent implements OnInit {
  protected files: any = {};
  protected currentFiles: any = [];
  protected serverId: string | null = null;
  protected currentPath: string = "";

  ngOnInit(): void {
    this.serverId = this.route.snapshot.paramMap.get('id');
    this.currentPath = "";

    var url =
      this.config.getApiBaseUrl() +
      this.config.getEndpoint('list_files') +
      `?id=${this.serverId}`;
    this.http.get(url).subscribe((response: any) => {
      this.files = response["data"];
      this.currentFiles = this.files[this.currentPath]["files"];
    });
  }

  redirectToFile(file: any): void {
    if (file.can_read) {
      this.router.navigate([`/server/${this.serverId}/files/${file.name}`]);
    }
  }

  constructor(
      private http: HttpClient,
      private config: ConfigService,
      private router: Router,
      private route: ActivatedRoute
    ) {}
}
