import { Component, OnInit } from '@angular/core';
import { StringService } from './services/string.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'opensouqfront';
  private distance: number;
  private firstString: string;
  private secondString: string;

  constructor(private stringService: StringService) {}

  ngOnInit() {
    this.distance = -1;
    this.firstString = '';
    this.secondString = '';
  }

  onClick(): void {
    this.stringService.postLevenstion(this.firstString, this.secondString).subscribe(
      res => {
        this.distance = res.levenstion;
      }
    );
  }
}
