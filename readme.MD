# TTCP CAGE Challenge 1
![Banner](/images/TTCP-Logo-small.png) ![Banner](/images/CAGE-Logo-small.png)

# Recorded Results

<table style="width: 150%">
    <thead>
        <tr>
            <th colspan="1" rowspan="3"></th>
        </tr>
        <tr>
            <th colspan="3">30 steps</th>
            <th colspan="3">50 steps</th>
            <th colspan="3">100 steps</th>
        </tr>
        <tr>
            <th>B-line</th>
            <th>Meander</th>
            <th>Sleep</th>
            <th>B-line</th>
            <th>Meander</th>
            <th>Sleep</th>
            <th>B-line</th>
            <th>Meander</th>
            <th>Sleep</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>Vanilla PPO</th>
        </tr>
        <tr>
            <td>10 episodes</td>
            <td>-8.71 ± 2.69</td>
            <td>-9.41 ± 4.20</td>
            <td>-0.5 ± 0.53</td>
            <td>-12.33 ± 3.87</td>
            <td>-33.98 ± 12.74</td>
            <td>-0.7 ± 0.82</td>
            <td>-40.27 ± 42.33</td>
            <td>-122.07 ± 38.79</td>
            <td>-0.9 ± 0.99</td>
        </tr>
        <tr>
            <td>1000 episodes</td>
            <td>-8.88 ± 5.46</td>
            <td>-11.09 ± 5.42</td>
            <td>-0.34 ± 0.59</td>
            <td>-15.21 ± 11.07</td>
            <td>-34.15 ± 14.75</td>
            <td>-0.52 ± 0.73</td>
            <td>-31.76 ± 25.05</td>
            <td>-110.54 ± 44.33</td>
            <td>-1.03 ± 2.7</td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>Vanilla DQN</th>
        </tr>
        <tr>
            <td>10 episodes</td>
            <td>-14.78 ± 3.41</td>
            <td>-12.46 ± 4.54</td>
            <td>-0.1 ± 0.32</td>
            <td>-42.37 ± 31.29</td>
            <td>-44.36 ± 30.93</td>
            <td>-0.5 ± 0.71</td>
            <td>-109.96 ± 61.09</td>
            <td>-144.74 ± 79.24</td>
            <td>-0.9 ± 0.88</td>
        </tr>
        <tr>
            <td>1000 episodes</td>
            <td>-16.81 ± 8.52</td>
            <td>-12.69 ± 5.62</td>
            <td>-0.361 ± 0.59</td>
            <td>-36.27 ± 21.05</td>
            <td>-40.84 ± 21.97</td>
            <td>-0.58 ± 0.74</td>
            <td>-103.21 ± 57.87</td>
            <td>-154.68 ± 68.76</td>
            <td>-1.11 ± 1.02</td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>Vanilla A2C</th>
        </tr>
        <tr>
            <td>10 episodes</td>
            <td>-15.14 ± 4.78</td>
            <td>-11.09 ± 5.59</td>
            <td>0.0 ± 0.0</td>
            <td>-32.23 ± 22.31</td>
            <td>-37.25 ± 29.92</td>
            <td>0.0 ± 0.0</td>
            <td>-65.41 ± 30.92</td>
            <td>-169.67 ± 50.90</td>
            <td>0.0 ± 0.0</td>
        </tr>
        <tr>
            <td>1000 episodes</td>
            <td>-15.81 ± 8.49</td>
            <td>-11.68 ± 5.83</td>
            <td>-0.01 ± 0.11</td>
            <td>-34.26 ± 20.89</td>
            <td>-38.28 ± 23.98</td>
            <td>-0.02 ± 0.14</td>
            <td>-96.39 ± 58.61</td>
            <td>-149.12 ± 79.14</td>
            <td>-0.04 ± 0.21</td>
        </tr>
    </tbody>
</table>


# Introduction

Recent advances in artificial intelligence \(AI\) technologies show promise for autonomous cyber operations \(ACO\), offering the potential for distributed, adaptive defensive measures at machine speed and scale\. The cyber domain is a particularly challenging domain for autonomous AI\. We nominate a challenge in this space which we believe requires further research in order to enable ACO to become an operational capability\. To facilitate this AI research, we, the TTCP[^1] CAGE[^2] Working Group, are releasing CybORG, an experimental platform using the OpenAI Gym interface together with a cyber security scenario and a challenge to which we invite researchers to respond\. 

[^1]: The Technical Cooperation Program (TTCP) is an international organisation that collaborates in defence scientific and technical information exchange; program harmonisation and alignment; and shared research activities in Australia, Canada, New Zealand, the United Kingdom and the United States of America.
[^2]: CAGE (Cyber Autonomy Gym for Experimentation) is a working group of TTCP that is aiming to support the development of AI tactics, techniques and procedures for cyber defence.

Our aim is to support the development of AI tactics, techniques and procedures with CybORG and a series of CAGE scenarios with associated challenge problems in order to support practical demonstrations of ACO\. We wish to engage the AI and cyber security research communities, especially to leverage domain experts outside of the cyber field, and by encapsulating the cyber elements in environments such as CybORG along with the CAGE scenarios and challenge problems, we hope that the cyber problem set becomes accessible to a wider audience\. The first CAGE scenario and associated challenge problem were released at the IJCAI\-21 1st International Workshop on Adaptive Cyber Defense \(ACD 2021\)\.

Our focus, which is rare in this area, is on the development of defensive cyber agents\. Rather than focusing on the detection of an attacker based on data, CybORG aims to develop the higher\-level strategies required to effectively respond to an attacker across an entire network\. Therefore, the defensive agents in CybORG select from a set of high\-level actions including the analysis of hosts, removal of malicious code and restoring of systems from backup\. In an extension to be released within the next two months, the defensive agents will also be able to employ deception on hosts, through the creation of decoy services\. Each action has costs, in terms of effort and system downtime, that must be balanced against the need to protect systems of differing importance from an attack\. For the purposes of the challenge, some red agents are provided for the defensive agents to train and be tested against\. 

# Scenario narrative

“There is an ongoing rivalry between neighbouring nations Guilder and Florin\. During a period of increasing tension between the two nations, Florin is receiving a significant increase of phishing attacks\. These attacks seem to be specifically targeted at factories manufacturing equipment for the Florin military\.

Cyber Threat Intelligence analysts have studied the attacks and believe that the attackers, potentially at the direction of Guilder, are attempting to disrupt the manufacture of a new weapon under development by Florin\. When the phishing attacks are successful, the attackers then use lateral movement to explore the network\. The ultimate goal of these attackers appears to be to compromise key operational systems that control aspects of the weapon system’s manufacturing\. This would cause delays in the delivery of the new weapon to the Florin military\.

Your firm has been contracted by Florin to trial your new autonomous defence agents\. Florin have given your agent authority to defend the computer network at one of their manufacturing plants\. The network, shown in Figure 1, contains a user network for staff, an enterprise network, and an operational network which contains the key manufacturing and logistics servers\. The defence agent receives an alert feed from Florin’s existing monitoring systems\. It can run detailed analyses on hosts, then remove malicious software if found\. If an attacker is too well established on a host to be removed, the host can be restored from a clean backup\. 

The network owner has undertaken an evaluation of the factory systems and contracted your firm to defend these systems according to the following criteria:

1. Maintain the critical operational server, so as to ensure information about the new weapon system is not revealed to Guilder and the production and delivery of the new weapon system remains on schedule\. 
2. Where possible, maintain enterprise servers so as to ensure day\-to\-day operations of the manufacturing plant are not disrupted or revealed\.”

# Challenge problem details

This challenge is designed for teams to create a blue agent to defend a network against a red agent, with a green agent representing the effect of network users\. The network is illustrated below in Figure 1\. It is divided into three subnets\. Subnet 1 consists of user hosts that are not critical\. Subnet 2 consists of enterprise servers designed to support the user activities on Subnet 1\. Subnet 3 contains the critical operational server and three user hosts\.

![Figure1](/images/figure1.png)

<p align="center">
 <em>Figure 1 Network of the scenario and challenge problem</em>
</p>

Each scenario run is a fixed number of steps representing a fixed period of time\. An episode will terminate only once the time expires\. At each step, the red and blue agents each choose one action from a set of high\-level actions that are described in Appendix A\. CybORG will take the chosen action and select a context\-appropriate low\-level action, such as modelling the behaviour of an operating system\-specific exploit in response to a high\-level exploit action by the red agent\. This is designed to reduce the action space and make a wider range of learning approaches tractable\.

The red agent starts each scenario run with an initial foothold: access to one of the user machines in Subnet 1\. The red agent can then choose actions to perform reconnaissance on hosts in the enterprise network \(Subnet 2\) and then exploit these hosts and perform privilege escalation\. Once they have exploited the server in the enterprise network that has the Operational Server IP address on it, they can access the operational network \(Subnet 3\)\. The Operational Server maintains a service that is key to the system owners’ operations; the goal of the red agent is to disrupt this service for as long as possible through the Impact action\.

In order to create a more robust blue agent, two red agents have been implemented, each with its own unique strategy\. The first has prior knowledge of the network layout and beelines straight to the Operational Server\. Another explores the network one subnet at a time, seeking to gain privileged access on all hosts in a subnet before moving on to the next one, eventually arriving at the Operational Server\.

The blue agent is assumed to start each scenario run with monitoring tools installed on all the user and server hosts\. It automatically receives data on new events that occur on these hosts\. It can use actions to perform more detailed analysis of hosts, giving it improved knowledge as to whether particular activity on a system is due to malicious activities of the red agent or benign activities of a green agent\. It can remove red access to hosts, or restore a system back to a standard configuration\. Removing red access only works if the red agent has not escalated their privilege on the system, as at this point it is assumed the red agent has sufficient access and persistence to recover from deleted processes or files\. Restoring a system is guaranteed to remove red agent activity, but restoring a system from a previously\-generated image is assumed to disrupt user activities on that system\. The red agent cannot be removed from the initial foothold system, even by the restore action – this assumption is made both as a means of ensuring the game lasts for the entire period, and to reflect the difficulty of eliminating a threat that has successfully phished credentials\. 

The effect of each action on the state of a targeted host is summarised in Figure 2\. 

![Figure2](/images/figure2.png)

<p align="center">
 <em>Figure 2 Effect of actions on host state (initial version)</em>
</p>

The green agent only performs the discovery action, and does not exploit hosts\. It should prevent the blue agent from assuming all network activity is due to the red agent\.

The order in which the agents choose and enact actions is blue, then green then red\. Before acting again, the blue agent receives an observation and reward based on the events that occurred as a result of the green and red actions\. 

The blue agent receives a negative reward any time the red agent gets administrator access to a system\. They continue to receive negative rewards as long as the red agent maintains administrator access\. The amount of each reward is dependent on the relative importance of that host to the confidentiality or availability of the entire system: -0\.1 and -1\.0 for low and high importance systems respectively \(see Table 1\)\. They also receive a negative reward if the red agent successfully uses the Impact action on the operational server \(\-10\) or the blue agent uses the restore action on any host \(\-1\) \(see Table 2\)\. The final score for a blue agent is the cumulative reward received by the agent over the course of the scenario run\.
 
*Table 1 Blue rewards for red administrator access \(per turn\)*
 
| Subnet   | Hosts              | Blue Reward for Red Access \(per turn\) |
|:--------:|:------------------:|:---------------------------------------:|
| Subnet 1 | User Hosts         | \-0\.1
| Subnet 2 | Enterprise Servers | \-1
| Subnet 3 | Operational Server | \-1
| Subnet 3 | Operational Hosts  | \-0\.1

*Table 2 Blue rewards for successful red actions \(per turn\)*

| Agent    | Hosts              | Action   | Blue Reward \(per turn\) |
|:--------:|:------------------:|:--------:|:------------------------:|
| Red      | Operational Server | Impact   | \-10
| Blue     | Any                | Restore  | \-1

# Challenge Extension

As an extension of the first challenge, version 1\.2 has an additional action of defensive deception for blue agents: Misinform\. This action will allow the blue agent to set up decoy services, intended to delay the red agent and provide a clear indicator of its behaviour when the red agent accesses them\. The effect of each action on the state in the second release is summarised in Figure 3\.

The Misinform action enables a decoy service, on a nominated host, which is vulnerable to exploitation by the red agent\. The probability of a red agent exploiting the decoy service versus a real service is given a fixed value of 75%\.

The decoy service is assumed to be monitored and secured such that an exploit of it does not allow further access to the host by the red agent\. Privilege Escalation actions using an exploited decoy service will automatically fail and will result in the removal of the red agent from that host\. To effectively exploit the system, the red agent must re\-exploit the host via a non\-decoy service\.

![Figure3](/images/figure3.png)

<p align="center">
 <em>Figure 3 Effect of actions on host state (extended version)</em>
</p>

# Instructions for obtaining environment

The CAGE challenge environment, CybORG, and first challenge are available here: [https://github\.com/cage\-challenge/cage\-challenge\-1/tree/main/CybORG](https://github.com/cage-challenge/cage-challenge-1/tree/main/CybORG)

The CAGE challenge is written in Python\. Dependencies can be installed using pip\. Further instructions are included on the GitHub page\. The challenge includes red agents to test against, and an example blue agent\. Submissions should implement the same methods of the example blue agent\.

# Instructions for submitting responses

Successful blue agents and any queries re the challenge can be submitted via email to: cage\.aco\.challenge@gmail\.com

When submitting a blue agent it should be for the extended version of the challenge, and teams should include:

- A team name and contact details\.
- The code implementing the agent, with a list of dependencies\.
- A description of your approach in developing a blue agent\.
- The files and terminal output of the evaluation function\.

 

We intend to publish the final results at the AAAI\-22 Workshop on Artificial Intelligence for Cyber Security \(AICS\)\. 

We also invite teams to submit full papers on their work on this CAGE challenge or using the CybORG environment to AAAI\-22, IJCAI\-22, or any other venue of their choice\. Please cite the challenge announcement as follows to reference the challenge:

```
@PROCEEDINGS{cage_challenge_announcement,
  author = {CAGE},
  Title = {CAGE Challenge 1},
  booktitle = {IJCAI-21 1st International Workshop on Adaptive Cyber Defense.} 
  Publisher = {arXiv},
  Year = {2021}
}
```

In addition, authors may reference the following paper that describes CybORG:

```
@PROCEEDINGS{cyborg_acd_2021,
  author = {Maxwell Standen, Martin Lucas, David Bowman, Toby J\. Richer, Junae Kim and Damian Marriott},
  Title = {CybORG: A Gym for the Development of Autonomous Cyber Agents},
  booktitle = {IJCAI-21 1st International Workshop on Adaptive Cyber Defense.} 
  Publisher = {arXiv},
  Year = {2021}
}
```

The challenge software can be referenced as:

```
@misc{cage_challenge_1,
  Title = {Cyber Autonomy Gym for Experimentation Challenge 1},
  Note = {Created by Maxwell Standen, David Bowman, Son Hoang, Toby Richer, Martin Lucas, Richard Van Tassel},
  Publisher = {GitHub},
  Howpublished = {\url{https://github.com/cage-challenge/cage-challenge-1}},
  Year = {2021}
}
```

## Evaluation of submissions

A leader board for submissions will be maintained until February 2022\. Final results will be announced at the close of the challenge via the GitHub site\.

The evaluation.py file is designed to provide a standardised evaluation for comparison that incorporates multiple different trial lengths and red agents\. These are:

- Trial Length: 30, 50, 100
- Red Agents: Meander \(explore randomly\), Beeline \(move directly to the operational server\), No Action \(sleep\)

For each combination of trial length and red agent, CybORG is run for 10 episodes and the total reward received by the blue agent is recorded for each episode\. The mean and standard deviation for each set of episodes are recorded in the evaluation file\.

The validation process involves summing the average scores of 1000 episodes for each combination of trial length and red agent\.  Those results will be published in the final leader board\.

## Important dates

20 August 2021: Challenge announced at ACD 2021 and open for submissions\.

2 December 2021: Release of extended version of the Challenge problem with a Misinform action available to the blue agent\.

~~1 February 2022: Challenge closed\.~~

7 February 2022 (any time zone): Updated final day for challenge submissions.

11 ~~4~~ February 2022: Final results announced\.

# Future challenges

The CAGE team will continue to develop this platform and plan to announce a new challenge problem after the close of this challenge\. Future topics may include expanded action sets, the introduction of multiple agents, and more complex and realistic scenarios\. 

# Appendix A - Blue Action Sets

| Action     | Purpose                                  | Parameters                                       | Output                                 |
|:-----------|:-----------------------------------------|:-------------------------------------------------|:---------------------------------------|
| Monitor | Collection of information about flagged malicious activity on the system\. Corresponds to action ID 1: Scan in the OpenC2 specification[^3]\. | None *\(Note: This action occurs automatically if another action is chosen\)* | Network connections and associated processes that are identified as malicious\. |
| Analyse | Collection of further information on a specific host to enable blue to better identify if red is present on the system\. Corresponds to action ID 30: Investigate in the OpenC2 specification\. | Hostname | Information on files associated with recent alerts including signature and entropy\.  |
| Misinform *(not in initial release)* | Setup of decoy services on a specific host\. Green agents do not access these services, so any access is a clear example of red activity\. | Hostname | An alert if the red agent accesses the new service\. |
| Remove | Attempting to remove red from a host by destroying malicious processes, files and services\. This action attempts to stop all processes identified as malicious by the monitor action\. Corresponds to action ID 10: Stop in the OpenC2 specification\. | Hostname  | Success/Failure |
| Restore | Restoring a system to a known good state\. This has significant consequences for system availability\. This action punishes Blue by \-1\. Corresponds to action ID 23: Restore in the OpenC2 specification\. | Hostname | Success/Failure  |

# Appendix B - Red Action Sets

| Action     | Purpose                                  | Parameters                                       | Output                                 |
|:-----------|:-----------------------------------------|:-------------------------------------------------|:---------------------------------------|
| Discover Remote Systems | ATT&CK[^4] Technique T1018 Remote System Discovery\. Discovers new hosts/IP addresses in the network through active scanning using tools such as ping\. | Subnet | IP addresses in the chosen subnet from hosts that respond to ping |
| Discover Network Services | ATT&CK Technique T1046 Network Service Scanning. Discovers responsive services on a selected host by initiating a connection with that host\. | Subnet | Ports and service information |
| Exploit Network Services | ATT&CK Technique T1210 Exploitation of Remote Services\. This action attempts to exploit services on a remote system\. | IP Address | Success/Failure <br /> Initial recon of host if successful <br /> Information on why failed \(unavailable port, etc\.\) |
| Escalate | ATT&CK Tactic TA0004 Privilege Escalation\. This action escalates the agent’s privilege on the host\. | Hostname | Success/Failure <p> Internal information now available due to increased access to the host |
| Impact | ATT&CK Technique T1489 Service Stop\. This action disrupts the performance of the network and fulfils red’s objective of denying the operational service\. | Hostname | Success/Failure  |


[^3]: Open Command and Control \(OpenC2\), [https://openc2\.org/](https://openc2\.org/)

[^4]: MITRE ATT&CK, [https://attack\.mitre\.org/](https://attack\.mitre\.org/)



