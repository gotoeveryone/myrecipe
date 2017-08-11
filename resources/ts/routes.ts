import { SearchComponent } from './components/cuisine-list/cuisine.component';
import { DetailComponent } from './components/cuisine-detail/detail.component';

export const ROUTES = [
    { path: '', component: SearchComponent },
    { path: 'add', component: DetailComponent },
    { path: 'edit/:id', component: DetailComponent },
];
