import { DetailComponent } from './components/cuisine-detail/detail.component';
import { SearchComponent } from './components/cuisine-list/cuisine.component';
import { LoginComponent } from './components/login/login.component';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { AuthGuardService } from './services/auth.service';

export const ROUTES = [
    {
        path: '',
        component: LoginComponent,
        pathMatch: 'full',
    },
    {
        path: 'cuisine',
        component: SearchComponent,
        canActivate: [AuthGuardService],
    },
    {
        path: 'cuisine/new',
        component: DetailComponent,
        canActivate: [AuthGuardService],
    },
    {
        path: 'cuisine/:id',
        component: DetailComponent,
        canActivate: [AuthGuardService],
    },
    {
        path: '**',
        component: NotFoundComponent,
    },
];
