import {Injectable} from '@angular/core';
import {Observable} from "rxjs";
import {AuthToken} from "../../models";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class LoginService {


  BASE_URL = 'http://localhost:8000'


  constructor(private client: HttpClient) {
  }

  logIn(username: string, password: string): Observable<AuthToken> {
    return this.client.post<AuthToken>(
      `${this.BASE_URL}/api/token/`,
      // http://127.0.0.1:8000/api/users/api/
      {username, password}
    )
  }

}
