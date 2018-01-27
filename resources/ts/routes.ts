import { DetailComponent } from './components/cuisine-detail/detail.component';
import { SearchComponent } from './components/cuisine-list/cuisine.component';

export const ROUTES = [
    { path: '', component: SearchComponent },
    { path: 'add', component: DetailComponent },
    { path: 'edit/:id', component: DetailComponent },
];
