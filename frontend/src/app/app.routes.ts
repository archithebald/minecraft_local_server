import { Routes } from '@angular/router';
import { ServersListComponent } from './servers-list/servers-list.component';
import { ServerPageComponent } from './server-page/server-page.component';
import { ServerOptionsPageComponent } from './server-options-page/server-options-page.component';
import { ServerConsolePageComponent } from './server-console-page/server-console-page.component';
import { CreateServerComponent } from './create-server/create-server.component';
import { ServerFilesPageComponent } from './server-files-page/server-files-page.component';

export const routes: Routes = [
  { path: '', redirectTo: 'servers', pathMatch: 'full' },
  { path: 'servers', component: ServersListComponent, pathMatch: 'full' },
  { path: 'server/:id', component: ServerPageComponent },
  { path: 'server/:id/options', component: ServerOptionsPageComponent },
  { path: 'server/:id/console', component: ServerConsolePageComponent },
  { path: 'server/:id/files', component: ServerFilesPageComponent },
  { path: 'create', component: CreateServerComponent, pathMatch: 'full' },
];
