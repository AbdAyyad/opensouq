import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { LeventionModel } from '../models/Levention.model';

@Injectable()
export class StringService {
    constructor(private http: HttpClient) {}

    postLevenstion(stringOne: string, stringTwo: string): Observable<LeventionModel> {
        const url = 'http://localhost:8000/api/levenstion/';
        const body = {string_one: stringOne, string_two: stringTwo};
        const options = {
            headers : new HttpHeaders({
                'Content-Type' : 'application/json'
            })
        };
        return this.http.post<LeventionModel>(url, body, options);
    }
}
